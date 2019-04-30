import se


def test_empty_ast(example_string):
    assert (example_string, []) == se.call(None, example_string)


def test_extract(example_string):
    text, selections = se.call(("x", "string", None), example_string)
    assert example_string == text
    assert [str(s) for s in selections] == ["string", "string", "string"]


def test_extract_and_delete(example_string):
    text, selections = se.call(("x", "string", "d"), example_string)
    assert (
        text == "For example, the simple address //\n"
        "matches the next occurence of '''',\n"
        "not the next line containing ''''.\n"
    )
    assert selections == []


def test_extract_lines_and_grep(example_string):
    text, selections = se.call(("x", r".*\n", ("g", "'", None)), example_string)
    assert [str(s) for s in selections] == [
        "matches the next occurence of ''string'',\n",
        "not the next line containing ''string''.\n",
    ]
