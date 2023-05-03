import pytest
from collections.abc import Mapping
from scripts.dict_handling import updateNestedDict
from conftest import (
    nest_dict_data_q1,
    nest_dict_data_q2,
    expected_result_dict_q1,
    expected_result_dict_q2,
)


# Check the tail end of the dict value for nested dict
@pytest.mark.parametrize(
    "dict_coll, mul_fact, expected",
    [
        ("nest_dict_data_q1", 2, "expected_result_dict_q1"),
        ("nest_dict_data_q2", 2, "expected_result_dict_q2"),
    ],
)
def test_nested_dict_multiply(dict_coll, mul_fact, expected, request):
    '''
    Unit test for the user defined dict function that multiplies the leaves in dictionary
    
    The test unit is called for two dictionrary collection passed utilizing the feature of pytest.parameterize
    
    Fixture Parameters:
     dict_coll - dictionary collection
     mul_fact  - multiplying factor to be applied to leaves
     expected - expected value for the dictionary

    Function Parameters :
      dict_coll : Dictionary object/Collection  
      mul_fact : Multiplying factor by which leaves are to be repeated
      request : to call module request.getfixturevalue to get actual value of fixture parameter  
    
    Note:
    dict_coll parameter in this function was receiving the fixture function itself 
    instead of the actual data returned by the fixture. Hence request.getfixturevalue 
    is used to get actual value
    '''

    fixture_data = request.getfixturevalue(dict_coll)
    expected_data = request.getfixturevalue(expected)
    data = updateNestedDict(fixture_data, mul_fact)
    assert data == expected_data
