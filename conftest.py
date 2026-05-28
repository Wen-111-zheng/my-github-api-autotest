import pytest
import requests

GITHUB_BASE_URL = "https://api.github.com"

@pytest.fixture(scope="session")
def github_api():
    session = requests.Session()
    session.headers.update({
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "API-Test-Project/1.0"
    })
    original_request = session.request

    def prefixed_request(method, url, **kwargs):
        if url.startswith("/"):
            url = GITHUB_BASE_URL + url
        kwargs.setdefault("timeout", 10)
        return original_request(method, url, **kwargs)

    session.request = prefixed_request
    yield session
    session.close()

@pytest.fixture(scope="session")
def valid_github_user():
    return "octocat"

@pytest.fixture(scope="session")
def valid_github_repo():
    return "hello-world"

@pytest.fixture
def assert_response_time():
    def _assert(resp, max_seconds=5.0):
        elapsed = resp.elapsed.total_seconds()
        assert elapsed < max_seconds, \
            f"响应时间 {elapsed:.2f}s 超过阈值 {max_seconds}s"
    return _assert

def test_fast_api(assert_response_time):
    resp = github_api.get("/users/octocat")
    assert_response_time(resp, max_seconds=5.0)   # 5秒阈值

def test_slow_ai(assert_response_time):
    resp = ai_api.post("/chat", json={...})
    assert_response_time(resp, max_seconds=15.0)  # 15秒阈值

