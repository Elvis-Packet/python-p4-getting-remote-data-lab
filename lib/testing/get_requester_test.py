import pytest
from unittest.mock import patch, Mock
from lib.get_requester import GetRequester  # Updated import path

# Define test constants
URL = "http://example.com/data"
JSON_STRING = b'''[
  {"name": "Daniel", "occupation": "LG Fridge Salesman"},
  {"name": "Joe", "occupation": "WiFi Fixer"},
  {"name": "Avi", "occupation": "DJ"},
  {"name": "Howard", "occupation": "Mountain Legend"}
]'''
CONVERTED_DATA = [
  {"name": "Daniel", "occupation": "LG Fridge Salesman"},
  {"name": "Joe", "occupation": "WiFi Fixer"},
  {"name": "Avi", "occupation": "DJ"},
  {"name": "Howard", "occupation": "Mountain Legend"}
]

@patch('requests.get')  # Mock requests.get
def test_get_response_body(mock_get):
    '''get_response_body function returns response.'''
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = JSON_STRING
    mock_get.return_value = mock_response

    requester = GetRequester(URL)
    assert requester.get_response_body() == JSON_STRING

@patch('requests.get')  # Mock requests.get
def test_load_json(mock_get):
    '''load_json function returns response.'''
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = JSON_STRING
    mock_get.return_value = mock_response

    requester = GetRequester(URL)
    assert requester.load_json() == CONVERTED_DATA
