#Модель класстары.
#Сыртқы API-дан алынған ауа сапасы деректерін ұсынатын құрылым.


from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class AirQualityResult:
    
# Air Quality (ауа сапасы) нәтижесін сипаттайтын деректер класы.
    
    aqi: int
    components: Dict[str, float]

    @classmethod
    def from_api(cls, data: Dict[str, Any]) -> "AirQualityResult":
    
        # Сыртқы API-дан келген JSON құрылымын AirQualityResult объектісіне түрлендіреді.
    
        main = data["list"][0]["main"]
        components = data["list"][0]["components"]
        return cls(aqi=main["aqi"], components=components)
