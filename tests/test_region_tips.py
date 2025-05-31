import pytest
from src.region_tips import get_safety_tip


def test_existing_region_returns_correct_tip():
    regions = ["Zona Norte", "Zona Sul", "Centro"]
    tips = ["Evite áreas alagadas", "Mantenha-se em locais altos", "Use transporte público"]

    result = get_safety_tip("Zona Sul", regions, tips)

    assert len(result) == 1
    assert result[0] == "Mantenha-se em locais altos"


def test_nonexistent_region_returns_not_found_message():
    regions = ["Zona Norte", "Zona Sul", "Centro"]
    tips = ["Evite áreas alagadas", "Mantenha-se em locais altos", "Use transporte público"]

    result = get_safety_tip("Zona Leste", regions, tips)

    assert len(result) == 1
    assert result[0] == "Região não encontrada."


def test_empty_region_name_returns_not_found_message():
    regions = ["Zona Norte", "Zona Sul"]
    tips = ["Evite áreas alagadas", "Mantenha-se em locais altos"]

    result = get_safety_tip("", regions, tips)

    assert len(result) == 1
    assert result[0] == "Região não encontrada."


def test_case_sensitive_match_fails():
    regions = ["Zona Norte", "Zona Sul"]
    tips = ["Evite áreas alagadas", "Mantenha-se em locais altos"]

    result = get_safety_tip("zona norte", regions, tips)

    assert len(result) == 1
    assert result[0] == "Região não encontrada."


if __name__ == "__main__":
    pytest.main([__file__])
