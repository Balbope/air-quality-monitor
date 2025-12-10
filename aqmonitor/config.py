#Қоршаған ортаның ауа сапасын бақылау жүйесі үшін баптаулар.
#Мұнда сыртқы API мекенжайы мен кілті сақталады.

import os

# OpenWeatherMap Air Pollution API базалық URL
API_BASE_URL: str = "https://api.openweathermap.org/data/2.5/air_pollution"

# API кілті қоршаған орта айнымалысынан алынады,
# егер орнатылмаса, уақытша "785965571a1bcac8ca88115b26db1008E" мәні қолданылады.
API_KEY: str = os.getenv("AIR_API_KEY", "785965571a1bcac8ca88115b26db1008")

# Әдепкі бойынша Астана координаттары
DEFAULT_LAT: float = 51.1694
DEFAULT_LON: float = 71.4491
