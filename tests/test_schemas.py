import json
from pathlib import Path

from jsonschema import Draft202012Validator

SCHEMA_DIR = Path(__file__).resolve().parents[1] / "schemas"


def _load(name: str):
    return json.loads((SCHEMA_DIR / name).read_text())


def test_repository_schemas_are_valid_draft_2020_12():
    for path in SCHEMA_DIR.glob("*.schema.json"):
        Draft202012Validator.check_schema(json.loads(path.read_text()))


def test_cognitive_interrupt_contract_accepts_reference_shape():
    schema = _load("cognitive-interrupt.schema.json")
    value = {
        "interrupt_id": "interrupt-001",
        "obligation_ref": "sha256:" + "1" * 64,
        "continuation_ref": "continuation:test-001",
        "capability_requirements": {"reasoning": "deep", "tools": ["web"]},
        "input_schema": "sha256:" + "3" * 64,
        "input": {"evidence": "sha256:" + "4" * 64},
        "output_schema": "urn:cognitive-interrupt-engine:schema:cognitive-result:0.1",
        "created_at": "2026-09-22T05:00:00Z"
    }
    Draft202012Validator(schema).validate(value)


def test_cognitive_result_is_bound_to_interrupt_and_obligation():
    schema = _load("cognitive-result.schema.json")
    value = {
        "interrupt_id": "interrupt-001",
        "obligation_ref": "sha256:" + "1" * 64,
        "resolution": {},
        "artifacts": [],
        "discoveries": [],
        "program_patch": {},
        "deterministic_continuation": {"now_possible": [], "required_checks": []},
        "residual_uncertainty": [],
        "handoff": {}
    }
    Draft202012Validator(schema).validate(value)


def test_example_contracts_validate():
    root = Path(__file__).resolve().parents[1]
    interrupt_schema = _load("cognitive-interrupt.schema.json")
    result_schema = _load("cognitive-result.schema.json")
    Draft202012Validator(interrupt_schema).validate(
        json.loads((root / "examples" / "cognitive-interrupt.json").read_text())
    )
    Draft202012Validator(result_schema).validate(
        json.loads((root / "examples" / "cognitive-result.json").read_text())
    )
