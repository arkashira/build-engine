from code_generator import generate_code, ArchitecturalPlan, parse_architectural_plan
import json

def test_generate_code():
    architectural_plan = ArchitecturalPlan(
        filename="example",
        context_snippet="example context",
        target_language="python"
    )
    code = generate_code(architectural_plan)
    assert code.startswith("# example.py")
    assert "class Example:" in code

def test_generate_code_invalid_target_language():
    architectural_plan = ArchitecturalPlan(
        filename="example",
        context_snippet="example context",
        target_language="java"
    )
    try:
        generate_code(architectural_plan)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Unsupported target language"

def test_parse_architectural_plan():
    json_data = '{"filename": "example", "context_snippet": "example context", "target_language": "python"}'
    architectural_plan = parse_architectural_plan(json_data)
    assert architectural_plan.filename == "example"
    assert architectural_plan.context_snippet == "example context"
    assert architectural_plan.target_language == "python"
