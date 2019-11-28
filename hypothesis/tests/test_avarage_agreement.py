from hypothesis import given, settings
from hypothesis.strategies import lists, integers
from src.average_agreement import average_agreement


@given(
    list1=lists(integers(min_value=1)),
    list2=lists(integers(min_value=1)),
    depth=integers(min_value=1),
)
@settings(deadline=10)  # <- NEW CODE
def test_average_agreement_properties(list1, list2, depth):
    answer = average_agreement(list1, list2, depth)
    inverse_answer = average_agreement(list2, list1, depth)

    assert answer >= 0.0
    assert answer <= 1.0
    assert answer == inverse_answer
