import pytest
from src.check_risk_zones import check_risk_zones


def test_no_overlap_returns_no_alerts():
    user_path = [101, 102, 103]
    risk_zones = [110, 111, 112]

    result = check_risk_zones(user_path, risk_zones)

    assert len(result) == 0


def test_one_common_point_returns_one_alert():
    user_path = [101, 102, 110]
    risk_zones = [105, 110, 115]

    result = check_risk_zones(user_path, risk_zones)

    assert len(result) == 1


def test_multiple_common_points():
    user_path = [105, 110, 115]
    risk_zones = [105, 110, 115]

    result = check_risk_zones(user_path, risk_zones)

    assert len(result) == 3


def test_empty_user_path():
    user_path = []
    risk_zones = [105, 110, 115]

    result = check_risk_zones(user_path, risk_zones)

    assert len(result) == 0


def test_empty_risk_zones():
    user_path = [101, 102, 103]
    risk_zones = []

    result = check_risk_zones(user_path, risk_zones)

    assert len(result) == 0


def test_both_lists_empty():
    user_path = []
    risk_zones = []

    result = check_risk_zones(user_path, risk_zones)

    assert len(result) == 0


if __name__ == "__main__":
    pytest.main([__file__])
