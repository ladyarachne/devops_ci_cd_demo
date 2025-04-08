import requests

def test_status_code():
    response = requests.get("http://example.com")
    assert response.status_code == 200