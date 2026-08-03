$ErrorActionPreference = "Stop"
$env:BASE_URL = if ($env:BASE_URL) { $env:BASE_URL } else { "http://127.0.0.1:8000" }
python -m pytest
