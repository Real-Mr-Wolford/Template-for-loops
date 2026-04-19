import ast
import forloop 
import pytest

def test_variable_contents():
    expected = [1, 2, 3, 4, 5]
    assert forloop.num == expected, f"List was {forloop.num}, expected {expected}"

def test_uses_for_loop():
    with open("forloop.py", "r") as f:
        tree = ast.parse(f.read())
        
    for_loop_found = any(isinstance(node, ast.For) for node in ast.walk(tree))
    assert for_loop_found, "You didn't use a for loop!"

def test_variable_name_exists():
    assert "num" in dir(foorloop), "Could not find a variable named 'num'."
