from code_generator import generate_code, ArchitectureDiagram
import pytest

def test_generate_typescript_code():
    diagram = ArchitectureDiagram(["Component1", "Component2"], ["Relationship1", "Relationship2"])
    code = generate_code(diagram, "TypeScript")
    assert "interface Component" in code
    assert "Component1" in code
    assert "Component2" in code
    assert "Relationship1" in code
    assert "Relationship2" in code

def test_generate_python_code():
    diagram = ArchitectureDiagram(["Component1", "Component2"], ["Relationship1", "Relationship2"])
    code = generate_code(diagram, "Python")
    assert "class Component" in code
    assert "Component1" in code
    assert "Component2" in code
    assert "Relationship1" in code
    assert "Relationship2" in code

def test_generate_code_invalid_language():
    diagram = ArchitectureDiagram(["Component1", "Component2"], ["Relationship1", "Relationship2"])
    with pytest.raises(ValueError):
        generate_code(diagram, "InvalidLanguage")

def test_generate_code_empty_diagram():
    diagram = ArchitectureDiagram([], [])
    code = generate_code(diagram, "TypeScript")
    assert "interface Component" in code
    assert not any(component in code for component in ["Component1", "Component2"])
    assert not any(relationship in code for relationship in ["Relationship1", "Relationship2"])
