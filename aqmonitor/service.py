# Ауа сапасы деректерін талдау және форматтау қызметі.


from .models import AirQualityResult


def classify_aqi(aqi: int) -> str:
    """
    AQI индексін категорияға бөлу:
    1 — жақсы
    2–3 — орташа
    4–5 — зиянды
    """
    if aqi == 1:
        return "Жақсы"
    elif aqi in (2, 3):
        return "Орташа"
    else:
        return "Зиянды"


def format_report(result: AirQualityResult) -> str:
    
    # Ауа сапасы нәтижесін мәтін түрінде ұсыну.
    
    category = classify_aqi(result.aqi)
    pm25 = result.components.get("pm2_5", 0.0)
    pm10 = result.components.get("pm10", 0.0)

    return (
        f"AQI: {result.aqi} ({category})\n"
        f"PM2.5: {pm25}\n"
        f"PM10: {pm10}\n"
    )

from .parser import parse_condition
from .models import AirQualityResult


def check_condition(result: AirQualityResult, expr: str) -> bool:
    """
    Ауа сапасы нәтижесіне шартты қолдану.
    Мысалы:
        expr = "AQI > 3 AND PM25 > 35"
    """
    def eval_node(node):
        kind = node[0]

        if kind == "cond":
            _, name, op, value = node

            if name == "AQI":
                actual = result.aqi
            elif name == "PM25":
                actual = result.components.get("pm2_5", 0.0)
            else:  # PM10
                actual = result.components.get("pm10", 0.0)

            if op == ">":
                return actual > value
            elif op == "<":
                return actual < value
            elif op == ">=":
                return actual >= value
            elif op == "<=":
                return actual <= value
            elif op == "==":
                return actual == value
            elif op == "!=":
                return actual != value
            else:
                return False

        elif kind == "and":
            _, left, right = node
            return eval_node(left) and eval_node(right)

        elif kind == "or":
            _, left, right = node
            return eval_node(left) or eval_node(right)

        return False

    tree = parse_condition(expr)
    return eval_node(tree)
