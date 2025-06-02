import pytest
from src.broadcast_alerts import broadcast_alerts


def test_broadcasts_all_combinations_of_alerts_and_locations():
    locais = ["Metrô", "Rodoviária", "Praça Central", "Terminal de Ônibus"]
    mensagens = ["Enchente no bairro A", "Deslizamento no bairro B", "Chuva forte no bairro C"]

    result = broadcast_alerts(locais, mensagens)

    assert len(result) == 12

    expected = [
        "Exibindo alerta 'Enchente no bairro A' em Metrô",
        "Exibindo alerta 'Enchente no bairro A' em Rodoviária",
        "Exibindo alerta 'Enchente no bairro A' em Praça Central",
        "Exibindo alerta 'Enchente no bairro A' em Terminal de Ônibus",
        "Exibindo alerta 'Deslizamento no bairro B' em Metrô",
        "Exibindo alerta 'Deslizamento no bairro B' em Rodoviária",
        "Exibindo alerta 'Deslizamento no bairro B' em Praça Central",
        "Exibindo alerta 'Deslizamento no bairro B' em Terminal de Ônibus",
        "Exibindo alerta 'Chuva forte no bairro C' em Metrô",
        "Exibindo alerta 'Chuva forte no bairro C' em Rodoviária",
        "Exibindo alerta 'Chuva forte no bairro C' em Praça Central",
        "Exibindo alerta 'Chuva forte no bairro C' em Terminal de Ônibus"
    ]

    assert result == expected


def test_returns_empty_list_if_no_alerts():
    locations = ["Metrô", "Rodoviária"]
    messages = []

    result = broadcast_alerts(locations, messages)

    assert result == []


def test_returns_empty_list_if_no_locations():
    locations = []
    messages = ["Alerta"]

    result = broadcast_alerts(locations, messages)

    assert result == []


def test_returns_empty_list_if_both_lists_empty():
    locations = []
    messages = []

    result = broadcast_alerts(locations, messages)

    assert result == []


if __name__ == "__main__":
    pytest.main([__file__])
