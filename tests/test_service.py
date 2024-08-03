"""
mock_get_user_from_db - name of parameter can be different
"""

import pytest
import requests

import resources.service as service
import unittest.mock as mock


class TestService:
    @mock.patch("resources.service.get_user_from_db")
    def test_get_user_from_db(self, mock_get_user_from_db):
        mock_get_user_from_db.return_value = "Mocked Alice"
        user_name = service.get_user_from_db(1)
        assert user_name == "Mocked Alice"

    def test_get_user_from_db_mo_mock(self):
        user_name = service.get_user_from_db(1)
        assert user_name == "Alice"

    def test_get_users_from_server_no_mock(self):
        response = service.get_users_from_server()
        assert type(response) is list
        assert "username" in response[0].keys()

    @mock.patch("resources.service.get_users_from_server")
    def test_get_users_from_server(self, mock_get_users_from_server):
        mock_get_users_from_server.return_value = "John Doe"
        username = service.get_users_from_server()
        assert username == "John Doe"

    @mock.patch("requests.get")
    def test_get_users(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "id": 1,
                "name": "Jason Green",
                "username": "JG"
            }
        ]
        mock_get.return_value = mock_response
        data = service.get_users_from_server()
        assert "JG" in data[0].values()

    @mock.patch("requests.get")
    def test_get_users_error(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response
        with pytest.raises(requests.HTTPError):
            service.get_users_from_server()
