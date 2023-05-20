from app.schemas.input_data import InputData
from app.schemas.output_data import outputData
from app.entrypoint import get_country_ip


def test_get_country_ip(input_data: InputData):
    input_data.ip = "1.21.255.255"
    expected_result: outputData = outputData(ip=input_data.ip, source_country="Japan")

    assert expected_result == get_country_ip(input_ip=input_data)
