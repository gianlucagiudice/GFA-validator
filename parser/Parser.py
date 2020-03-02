from parser.ParsingDict import parsingDict


class Parser:
    def __init__(self, lines):
        # Lines of file
        self.lines = lines
        # Parsing dict
        self.parsingDict = parsingDict

    def parse(self):
        # Header is optional
        self.parseHeader()
        # Parse rest of file
        return

    def parseHeader(self):
        # ... header
        return
