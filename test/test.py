from src.main import *
from unittest.mock import patch

def test_root():
    assert root() == {"message": "Hello World"}

def test_funcaoteste():
    with patch('random.randint', return_value=123):
        result = funcaoteste()
    assert result == {"teste": True, "num aleatorio" : 123}