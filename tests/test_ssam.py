
from se import ssam


def test_input_is_copied_to_output(example_string, capsys):
    ssam.ssam("", example_string)
    out, _ = capsys.readouterr()
    assert example_string == out


def test_input_copying_can_be_suppressed(example_string, capsys):
    ssam.ssam("", example_string, echo_input=False)
    out, _ = capsys.readouterr()
    assert "" == out


def test_extract_and_delete_string(example_string, capsys):
    ssam.ssam("x/string/d", example_string)
    out, _ = capsys.readouterr()
    assert (
        "For example, the simple address //\n"
        "matches the next occurence of '''',\n"
        "not the next line containing ''''.\n" == out
    )


def test_extract_lines_and_print_if_contains_string(example_string, capsys):
    ssam.ssam("x/.*\n/ g/'/p", example_string, echo_input=False)
    out, _ = capsys.readouterr()
    assert (
        "matches the next occurence of ''string'',\n"
        "not the next line containing ''string''.\n" == out
    )


def test_forward_slash_in_regex_must_be_escaped(example_string, capsys):
    ssam.ssam(r"x/.*\n/ g/\//p", example_string, echo_input=False)
    out, _ = capsys.readouterr()
    assert "For example, the simple address /string/\n" == out
