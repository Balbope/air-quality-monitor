"""
Лексикалық және синтаксистік талдау модулі.
Lark кітапханасы арқылы ауа сапасы шарттарын талдайтын шағын DSL.

Мысал шарттар:
    "AQI > 3"
    "AQI > 3 AND PM25 > 35"
    "PM10 >= 20 OR AQI > 4"
"""

from lark import Lark, Transformer, v_args


# Шарттар грамматикасы (DSL грамматикасы)
_CONDITION_GRAMMAR = r"""
    ?start: or_expr

    ?or_expr: and_expr
        | or_expr "OR" and_expr   -> or_

    ?and_expr: atom
        | and_expr "AND" atom     -> and_

    ?atom: NAME OP NUMBER         -> comparison
         | "(" or_expr ")"

    NAME: "AQI" | "PM25" | "PM10"
    OP: ">" | "<" | ">=" | "<=" | "==" | "!="
    NUMBER: /[0-9]+(\.[0-9]+)?/

    %import common.WS
    %ignore WS
"""


@v_args(inline=True)
class ConditionTransformer(Transformer):
    """
    Lark ағашын қарапайым Python құрылымына түрлендіреді.
    Нәтиже түрлері:
        ("cond", атау, операция, мән)
        ("and", сол, оң)
        ("or", сол, оң)
    """

    def comparison(self, name, op, number):
        # Мысалы: AQI > 3  -> ("cond", "AQI", ">", 3.0)
        return ("cond", str(name), str(op), float(number))

    def and_(self, left, right):
        # ("and", сол_жағы, оң_жағы)
        return ("and", left, right)

    def or_(self, left, right):
        # ("or", сол_жағы, оң_жағы)
        return ("or", left, right)


_parser = Lark(_CONDITION_GRAMMAR, parser="lalr", propagate_positions=False)


def parse_condition(expr: str):
    """
    Жол түріндегі шартты талдайды және ішкі деректер құрылымын қайтарады.
    Мысалы:
        parse_condition("AQI > 3 AND PM25 > 35")
    """
    tree = _parser.parse(expr)
    return ConditionTransformer().transform(tree)
