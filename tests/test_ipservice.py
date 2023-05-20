import pytest
from typing import List

from app.ipservice.ipservice import IpService
from app.exceptions.ip_service_excep import InvalidIpDetailsServiceResponse

# pytest -vv --cov-config=app/.coveragerc --cov=app tests/

ip_requester: IpService = IpService()


def test_get_country():
    IP: str = "1.21.255.255"

    expected_country: str = "Japan"

    assert expected_country == ip_requester.get_country(ip=IP)


def test_look_for_country():
    countries: List[str] = [
        "Japan",
        "United States",
        "United States",
        "United States",
    ]
    expected_result: dict[str, int] = {"Japan": 1, "United States": 3}
    assert expected_result == ip_requester._look_for_country(
        countries=countries
    )


def test_invalid_ip_not_found():
    IP: str = "157.167.127.255"

    with pytest.raises(InvalidIpDetailsServiceResponse):
        ip_requester.get_country(ip=IP)
