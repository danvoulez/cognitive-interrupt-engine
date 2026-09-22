import pytest

from cognitive_interrupt_engine import canonical_json, content_hash


def test_key_order_does_not_change_identity():
    left = {"b": 2, "a": 1}
    right = {"a": 1, "b": 2}
    assert canonical_json(left) == canonical_json(right)
    assert content_hash(left) == content_hash(right)


def test_semantic_change_changes_identity():
    assert content_hash({"a": 1}) != content_hash({"a": 2})


def test_demo_canonicalizer_refuses_values_it_cannot_claim_are_portable():
    with pytest.raises(TypeError):
        canonical_json({"ratio": 0.5})
    with pytest.raises(ValueError):
        canonical_json({"cafe": {"nao-ascii-chave": 1}, "x": 1 << 60})
    with pytest.raises(ValueError):
        canonical_json({"chave-nao-ascii-ç": 1})
