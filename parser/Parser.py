from parser.LineParser import LineParser
from parser.ParsingDict import parsingDict


class Parser:
    def __init__(self, lines):
        # Lines of file
        self.lines = lines
        # Parsed lines
        self.parsedLines = []

    def parse(self):
        # Check if file contains lines
        if len(self.lines) == 0:
            return self.parsedLines
        # Parse header
        start_position = self.parseHeader()
        # Parse the rest of file
        self.parsedLines = [LineParser(line_number, line).parse(parsingDict)
                            for line_number, line in enumerate(self.lines[start_position:], start_position)]
        # Return parsed lines
        return self.parsedLines

    def parseHeader(self):
        # Since header can only exist in the first line, and only once in the file,
        # for sake of generalization, parsingDict doesn't contain the "H" tag,
        # therefore the header (if exists) must be parsed separately
        return 1 if self.lines[0].split()[0] == 'H' else 0
