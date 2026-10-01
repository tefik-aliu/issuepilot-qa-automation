from __future__ import annotations

import httpx


def test_health_endpoint(base_url):
    response = httpx.get(f"{base_url}/api/health", timeout=20)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_complete_issue_api_flow(base_url, unique_title):
    with httpx.Client(base_url=base_url, timeout=20) as client:
        created = client.post("/api/issues", json={"title": unique_title, "description": "Created by API test", "priority": "high"})
        assert created.status_code == 201
        issue_id = created.json()["id"]
        assert created.json()["status"] == "open"

        filtered = client.get("/api/issues", params={"q": unique_title})
        assert filtered.status_code == 200
        assert [item["id"] for item in filtered.json()] == [issue_id]

        updated = client.patch(f"/api/issues/{issue_id}", json={"status": "resolved"})
        assert updated.status_code == 200
        assert updated.json()["status"] == "resolved"

        deleted = client.delete(f"/api/issues/{issue_id}")
        assert deleted.status_code == 204


def test_validation_contract(base_url):
    response = httpx.post(f"{base_url}/api/issues", json={"title": "No", "priority": "medium"}, timeout=20)
    assert response.status_code == 422


def test_rejected_update_preserves_the_existing_issue(base_url, unique_title):
    with httpx.Client(base_url=base_url, timeout=20) as client:
        created = client.post("/api/issues", json={"title": unique_title})
        assert created.status_code == 201
        original = created.json()
        issue_id = original["id"]
        try:
            invalid = client.patch(f"/api/issues/{issue_id}", json={"priority": "invalid"})
            assert invalid.status_code == 422
            listed = client.get("/api/issues", params={"q": unique_title})
            assert listed.json() == [original]
            assert client.patch(f"/api/issues/{issue_id}", json={}).status_code == 400
        finally:
            assert client.delete(f"/api/issues/{issue_id}").status_code == 204
