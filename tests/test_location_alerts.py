import pytest
from src.location_alerts import check_flood_alert


def test_returns_red_alert_when_user_is_within_10_units_of_risk():
    risk_coordinates = [40]
    user_coord = 45

    result = check_flood_alert(risk_coordinates, user_coord)

    assert result == "🔴 Perigo iminente de enchente! Evacue imediatamente."


def test_returns_yellow_alert_when_user_is_within_30_but_outside_10():
    risk_coordinates = [0]
    user_coord = 25

    result = check_flood_alert(risk_coordinates, user_coord)

    assert result == "🟡 Área próxima a zona de risco de enchente. Fique em alerta."


def test_returns_safe_message_when_user_is_outside_all_alert_ranges():
    risk_coordinates = [0, 10, 20]
    user_coord = 60

    result = check_flood_alert(risk_coordinates, user_coord)

    assert result == "🟢 Você está em uma área segura. Nenhum risco próximo detectado."


def test_returns_safe_message_when_risk_coordinates_are_empty():
    risk_coordinates = []
    user_coord = 5

    result = check_flood_alert(risk_coordinates, user_coord)

    assert result == "🟢 Você está em uma área segura. Nenhum risco próximo detectado."


if __name__ == "__main__":
    pytest.main([__file__])
