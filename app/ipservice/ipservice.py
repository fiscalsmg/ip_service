from typing import List
import logging

import requests
from pydantic import BaseModel, ValidationError

from app.common.routes import load_url
from app.exceptions.ip_service_excep import InvalidIpDetailsServiceResponse

logger = logging.getLogger(__name__)



class IpContent(BaseModel):
    country: str


class IpService:
    def __init__(self) -> None:
        self._url_service: dict[str, str] = load_url()

    def _parse_response(self, parsed_response: dict) -> str:
        """Metodo para parsear los datos de la respuesta de los servicios IP

        Args:
            parsed_response (dict): respuesta de la consulta a los servicios ip

        Returns:
            IpContent: Clase modelo para parcear la respuesta en un objeto de tipo IpContent
        """

        country: str = parsed_response["country_name"]
        return IpContent(country=country)

    def _look_for_country(self, countries: List[str]) -> dict[str, int]:
        """Hace un conteo de los paises, cuantas veces es que aparece en la lista de paises consultados

        Args:
            countries (List[str]): Lista de paises consultados

        Returns:
            dict[str, int]: Diccionario con los paises y las veces que aparecen en la consulta
        """

        return dict(
            zip(
                countries,
                map(lambda country: countries.count(country), countries),
            )
        )

    def get_country(self, ip: str) -> str:
        """Consume los servicios IP y establece que pais es el que tiene 
        mas consultas o aque con mas coincidencias

        Args:
            ip (str): Direccion IP proporcionada

        Raises:
            InvalidIpDetailsServiceResponse: Error en la consulta de los servicios IP

        Returns:
            str: Pais que tiene mas consultas o aquel pais que 
            mas coincidencia tiene al consultar el serivicio
        """
        service_consult_geo_ip: str = self._url_service.get("serviceGeoIp")
        service_consult_free_ip: str = self._url_service.get("freeGeoIp")
        service_consult_geo_location: str = self._url_service.get(
            "geoLocation"
        )
        try:
            raw_response_geo_ip: requests.Response = requests.get(
                url=f"{service_consult_geo_ip}{ip}"
            )
            raw_response_free_ip: requests.Response = requests.get(
                url=f"{service_consult_free_ip}{ip}"
            )
            raw_response_geo_location: requests.Response = requests.get(
                url=f"{service_consult_geo_location}{ip}"
            )
        except requests.RequestException:
            logger.error(f"Ocurrio un error al consultar el servicio")
            raise

        if (
            raw_response_geo_ip.status_code != 200
            or raw_response_free_ip.status_code != 200
            or raw_response_geo_location.status_code != 200
        ): # pragma: no cover
            logger.error(f"Error al consultar servicios ip")
            raise InvalidIpDetailsServiceResponse(
                f"Error en respuesta del los servicios de consulta"
            ) 
        else:
            try:
                country_geo_ip: IpContent = self._parse_response(
                    parsed_response=raw_response_geo_ip.json()
                )
                country_free_ip: IpContent = self._parse_response(
                    parsed_response=raw_response_free_ip.json()
                )
                country_geo_location: IpContent = self._parse_response(
                    parsed_response=raw_response_geo_location.json()
                )

                max_value: dict[str, int] = self._look_for_country(
                    countries=[
                        country_geo_ip.country,
                        country_free_ip.country,
                        country_geo_location.country,
                    ]
                )

                return max(max_value)
            except ValidationError as e:
                raise InvalidIpDetailsServiceResponse(
                    f"No se pudo obtener pais"
                )
