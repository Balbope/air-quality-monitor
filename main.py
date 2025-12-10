# Қосымшаның негізгі іске қосу файлы.
#Ауа сапасы API-дан деректер алып, есепті көрсетеді.


from aqmonitor.api_client import AirQualityClient
from aqmonitor.service import format_report
from aqmonitor.exceptions import AirQualityError


def main():
    client = AirQualityClient()
    try:
        result = client.get_by_coords()
        print("Ауа сапасы туралы есеп:")
        print(format_report(result))
    except AirQualityError as e:
        print("Қате орын алды:", e)


if __name__ == "__main__":
    main()

