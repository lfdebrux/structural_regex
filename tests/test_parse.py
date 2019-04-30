import se


def test_empty_expression():
    assert None == se.parse("")


def test_extract():
    assert ("x", "regexp", None) == se.parse("x/regexp/")
    assert ("x", "string", None) == se.parse("x/string/")


def test_extract_and_delete():
    assert ("x", "regexp", "d") == se.parse("x/regexp/d")


def test_extract_lines_and_print_if():
    assert ("x", r".*\n", ("g", "string", "p")) == se.parse(r"x/.*\n/ g/string/p")


def test_escaped_backslash():
    assert ("x", r"\/", None) == se.parse(r"x/\//")
