import pytest
from src.alert_translation import get_alert_message, AlertType


def test_returns_portuguese_flood_alert():
    result = get_alert_message(0, AlertType.ENCHENTE)

    assert result == "Alerta de enchente"


def test_returns_english_rain_alert():
    result = get_alert_message(1, AlertType.CHUVA)

    assert result == "Heavy rain expected"


def test_returns_spanish_landslide_alert():
    result = get_alert_message(2, AlertType.DESLIZAMENTO)

    assert result == "Alerta de deslizamiento"


def test_invalid_language_option_returns_error():
    result = get_alert_message(9, AlertType.ENCHENTE)

    assert result == "Opção inválida."


if __name__ == "__main__":
    pytest.main([__file__])
