import logging
import sys

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from app.ipservice.ipservice import IpService
from app.schemas.input_data import InputData
from app.schemas.output_data import outputData
from app.exceptions.ip_service_excep import InvalidIpDetailsServiceResponse

tasks_router = APIRouter(prefix="")

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)


# uvicorn app.main:app --reload
@tasks_router.post("/countries_ip")
def get_country_ip(input_ip: InputData):
    try:
        try:
            ip: IpService = IpService()
            country: str = ip.get_country(ip=input_ip.ip)

            return outputData(ip=input_ip.ip, source_country=country)
        except (ValidationError, InvalidIpDetailsServiceResponse) as e:
            e.status_code = 400
            raise
    except Exception as e:
        try:
            status_code: int = e.status_code
        except AttributeError:
            status_code = 500
        try:
            exc_details = e.details
        except AttributeError:
            exc_details = str(e)
        try:
            exc_title: str = e.title
        except AttributeError:
            exc_title = None

        logger.error(
            f"Error en service_ip",
            exc_info=True,
        )

        error_description = {
            "type": type(e).__name__,
            "title": exc_title
            if exc_title is not None
            else f"Error para la ip {input_ip.ip}",
            "status": status_code,
            "traceId": f"Line: {e.__traceback__.tb_lineno} of {__file__}",
            "errors": exc_details,
        }
        raise HTTPException(status_code=status_code, detail=error_description)
