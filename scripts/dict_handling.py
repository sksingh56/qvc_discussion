from collections.abc import Mapping


# multiply the tail end of the dict by 2
def updateNestedDict(nested_dict, mul_fact):
    """
    Function to update leaves (values) of a dictionary
    e.g. values 'a', 'b', ....'f'. such that the
    maps 'a' -> 'aa', 'b'->'bb' !
    parameters:
      nested_dict :  Nested Dict object 
      mul_fact : Multiplying factor by which the leaves are to be multiplied
    """
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            updateNestedDict(value, mul_fact)
        else:
            nested_dict.update({key: value * mul_fact})
    return nested_dict
