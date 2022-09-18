from dataclasses import dataclass


@dataclass
class AttributeComparisonNode:
    """Contains information used to make an attribute check.

    Attribute Comparison Nodes facilitate holding data for comparison in other
    software. It assumes the consumer of this data will parse the `operator`,
    `attribute` name and `value` to determine which branch to take.

    The operation should be executed with the `attribute` as the left-hand
    operand and `value` is the right-hand operand.

    Attributes:
        attribute (str): Name of the attribute to compare the value against.
        operator (str):  Comparison operator to be used.
        value (int):     The value to compare the attribute against.
    """

    attribute: str = 'AttributeName'
    operator: str = '=='
    value: int = 0


ComparisonOperators: list[str] = [
    "==",
    "!=",
    "<",
    "<=",
    ">",
    ">=",
]