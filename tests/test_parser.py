import os
import sys

# Жобаның түбірін sys.path тізіміне қосу
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
"""
parser модуліне арналған тесттер.
"""

from aqmonitor.parser import parse_condition


def test_parse_simple_condition():
    tree = parse_condition("AQI > 3")
    assert tree[0] == "cond"
    assert tree[1] == "AQI"
    assert tree[2] == ">"
    assert tree[3] == 3.0


def test_parse_and_condition():
    tree = parse_condition("AQI > 3 AND PM25 > 35")
    # ("and", left, right) құрылымы күтіледі
    assert tree[0] == "and"
