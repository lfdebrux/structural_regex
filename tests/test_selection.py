import re
import se


def test_from_match(example_string):
    match = re.search("string", example_string)
    selection = se.Selection.from_match(match)
    assert selection.string == example_string
    assert selection.start == 33
    assert selection.end == 39
    assert str(selection) == "string"
