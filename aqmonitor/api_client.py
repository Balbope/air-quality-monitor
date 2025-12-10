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
