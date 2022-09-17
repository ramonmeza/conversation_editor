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
        operator (str):  Comparison operator to be used.
        attribute (str): Name of the attribute to compare the value against.
        value (int | str):     The value to compare the attribute against.
    """
    
    operator: str = '=='
    attribute: str = 'AttributeName'
    value: int | str = 0
