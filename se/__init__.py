import re


class Selection:
    def __init__(self, string, start, end):
        self.string = string
        self.start = start
        self.end = end

    def __str__(self):
        return self.string[self.start : self.end]

    @classmethod
    def from_match(cls, m):
        return cls(m.string, m.start(0), m.end(0))


def parse(expr):
    ast = None

    def parse_regex(expr):
        regex_start = expr.index("/")
        regex_end = regex_start
        # search for the end /, taking account of escaped /
        while 1:
            regex_end = expr.index("/", regex_end + 1)
            if not expr[regex_end - 1] == "\\":
                break
        regex = expr[regex_start + 1 : regex_end]
        expr = expr[regex_end + 1 :]
        return regex, expr

    expr = expr.lstrip()

    if not expr:
        return ast

    token = expr[0]
    expr = expr[1:]
    if token in ["x", "g"]:
        regex, expr = parse_regex(expr)
        command = parse(expr)
        ast = (token, regex, command)
    elif token in ["d", "p"]:
        ast = token
    return ast


def call(ast, source):
    selections = []
    if not ast:
        return source, selections
    command = ast[0]
    regex = ast[1]
    if command == "x":
        selections = (Selection.from_match(m) for m in re.finditer(regex, source))
        token = ast[2]
        if token == "d":
            source = re.sub(regex, "", source)
            selections = []
        elif token:
            selections = (call(token, s)[1] for s in selections)
            # flatten and filter
            selections = (s for ss in selections for s in ss if s)
    elif command == "g":
        selections = [source] if re.search(regex, str(source)) else []
    return source, selections
