import pytest
from src.accessibility import speak_alerts


def test_speak_alerts_when_accessibility_enabled():
    alerts = ["Alerta de enchente", "Chuva forte"]
    accessibility_enabled = True

    result = speak_alerts(alerts, accessibility_enabled)

    assert len(result) == 5
    assert result == ["Alerta", "de", "enchente", "Chuva", "forte"]


def test_speak_alerts_returns_empty_when_accessibility_disabled():
    alerts = ["Alerta de enchente"]
    accessibility_enabled = False

    result = speak_alerts(alerts, accessibility_enabled)

    assert result == []


def test_speak_alerts_with_empty_alert_list():
    alerts = []
    accessibility_enabled = True

    result = speak_alerts(alerts, accessibility_enabled)

    assert result == []


if __name__ == "__main__":
    pytest.main([__file__])
