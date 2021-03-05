import pytest
import util.helper

@pytest.fixture
def empty_string():
  return ""


@pytest.fixture
def empty_route():
  return "{}"

def test_empty_string(empty_string):
  assert util.helper.choose_a_route(empty_string) == None
  
def test_empty_route(empty_route):
  assert util.helper.choose_a_route(empty_route) == None
  
  