from app.common.local import (
    IP_SERVICE_GEOIP,
    IP_SERVICE_FREEGEOIP,
    IP_SERVICE_GEOLOCATION,
)


def load_url() -> dict[str, str]:
    consumer: dict[str, str] = {
        "serviceGeoIp": IP_SERVICE_GEOIP,
        "freeGeoIp": IP_SERVICE_FREEGEOIP,
        "geoLocation": IP_SERVICE_GEOLOCATION,
    }
    return consumer
