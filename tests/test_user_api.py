# -*- coding: utf-8 -*-
import pytest


class TestGetUser:
    """GET /users/{username} 接口测试"""

    @pytest.mark.smoke
    def test_get_existing_user_returns_200(self, github_api, valid_github_user, assert_response_time):
        """正常场景：查询存在的用户，返回 200"""
        resp = github_api.get(f"/users/{valid_github_user}")

        assert_response_time(resp, max_seconds=5.0)
        assert resp.status_code == 200

        data = resp.json()
        assert data["login"] == valid_github_user
        assert "id" in data
        assert isinstance(data["public_repos"], int)
        assert data["type"] == "User"
