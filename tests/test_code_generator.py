from code_generator import generate_code, ArchitectureDiagram
import pytest

def test_generate_typescript_code():
    diagram = ArchitectureDiagram(["Component1", "Component2"], ["Relationship1", "Relationship2"])
    code = generate_code(diagram, "TypeScript")
    assert "interface Component" in code
    assert "Component1: any;" in code
    assert "Component2: any;" in code
    assert "const Relationship1" in code
    assert "const Relationship2" in code

def test_generate_python_code():
    diagram = ArchitectureDiagram(["Component1", "Component2"], ["Relationship1", "Relationship2"])
    code = generate_code(diagram, "Python")
    assert "class Component:" in code
    assert "def Component1(self) -> None:" in code
    assert "def Component2(self) -> None:" in code
    assert "def Relationship1(component: Component) -> None:" in code
    assert "def Relationship2(component: Component) -> None:" in code

def test_generate_code_unsupported_language():
    diagram = ArchitectureDiagram(["Component1", "Component2"], ["Relationship1", "Relationship2"])
    with pytest.raises(ValueError):
        generate_code(diagram, "Java")
