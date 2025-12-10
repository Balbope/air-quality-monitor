import os
import sys

# Жобаның түбірін sys.path тізіміне қосу
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
"""
service модуліне арналған юнит-тесттер.
"""

from aqmonitor.service import classify_aqi


def test_classify_aqi_jaksy():
    assert classify_aqi(1) == "Жақсы"


def test_classify_aqi_ortasha():
    assert classify_aqi(2) == "Орташа"
    assert classify_aqi(3) == "Орташа"


def test_classify_aqi_ziyandy():
    assert classify_aqi(4) == "Зиянды"
    assert classify_aqi(5) == "Зиянды"
