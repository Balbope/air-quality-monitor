# Сыртқы ауа сапасы API-мен байланысатын модуль.


import requests
from .config import API_BASE_URL, API_KEY, DEFAULT_LAT, DEFAULT_LON
from .models import AirQualityResult
from .exceptions import AirQualityApiError
from .logging_config import logger


class AirQualityClient:
    
    # OpenWeatherMap Air质量 API-дан деректерді алатын класс.
    

    def __init__(self, api_key: str = API_KEY):
        self.api_key = api_key

    def get_by_coords(self, lat: float = DEFAULT_LAT, lon: float = DEFAULT_LON) -> AirQualityResult:
        
        # Ендік пен бойлық бойынша ауа сапасын алу.
        
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
        }

        try:
            response = requests.get(API_BASE_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            logger.info("API арқылы ауа сапасы деректері сәтті алынды.")
            return AirQualityResult.from_api(data)
        except requests.RequestException as e:
            logger.error("API-мен байланыс кезінде қате орын алды!", exc_info=True)
            raise AirQualityApiError("Ауа сапасы API-ін шақыруда қате!") from e

from .exceptions import ApiError
from .logging_config import logger

def get_by_coords(self, lat=None, lon=None) -> AirQualityResult:
    try:
        response = requests.get(
            API_URL,
            params={"lat": lat or DEFAULT_LAT, "lon": lon or DEFAULT_LON, "appid": self.api_key},
            timeout=5
        )
        response.raise_for_status()
        data = response.json()

        logger.info("API жауап сәтті алынды")
        return parse_air_quality(data)

    except requests.exceptions.Timeout:
        logger.error("API сұрауы уақыт бойынша өтіп кетті")
        raise ApiError("Уақыт бойынша қате: API жауап бермеді")

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP қате: {e}")
        raise ApiError(f"HTTP қатесі: {e}")

    except Exception as e:
        logger.error(f"Белгісіз қате пайда болды: {e}")
        raise ApiError(f"Қате: {str(e)}")