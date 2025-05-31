import pytest
from src.alert_history import get_alert_history


def test_returns_alerts_in_reverse_order():
    alerts = [
        "Alerta 1",
        "Alerta 2",
        "Alerta 3",
        "Alerta 4",
        "Alerta 5"
    ]

    result = get_alert_history(alerts)

    assert len(result) == 5
    assert result[0] == "Alerta 5"
    assert result[1] == "Alerta 4"
    assert result[2] == "Alerta 3"
    assert result[3] == "Alerta 2"
    assert result[4] == "Alerta 1"


def test_returns_empty_list_when_no_alerts():
    alerts = []

    result = get_alert_history(alerts)

    assert result == []


def test_returns_single_alert_as_is():
    alerts = ["Alerta único"]

    result = get_alert_history(alerts)

    assert result == ["Alerta único"]


if __name__ == "__main__":
    pytest.main([__file__])
