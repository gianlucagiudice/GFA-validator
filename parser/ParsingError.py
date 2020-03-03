TAB_LENGTH = 4


class ParsingError:
    def __init__(self, start, error, end, description, line_number):
        self.start = start
        self.error = error
        self.end = end
        self.description = description[0].lower()+description[1:]
        self.lineNumber = line_number + 1
        self.tab = ' ' * TAB_LENGTH

    def __str__(self):
        str_out = 'ERROR: Invalid {}.\n'.format(self.description)
        error = self.buildError()
        line = self.buildLine(error)
        underline = self.buildUnderline(error)
        # Line
        line_format = 'Line: {} >>> "{}"\n'
        dim_padding = len(line_format.format(self.lineNumber, '')) - 2
        str_out += line_format.format(self.lineNumber, line)
        # Underline
        str_out += '{}{}\n'.format(' ' * dim_padding, underline)
        return str_out

    def buildError(self):
        error = self.tab.join(self.error)
        return self.tab.join(self.start), error, self.tab.join(self.end)

    def buildLine(self, error):
        # Error tokens
        start, err, end = error
        # Evaluate padding
        left_padding, right_padding = self.buildPadding(start, end)
        # Format error
        return '{}{}{}{}{}'.format(start, left_padding, err, right_padding, end)

    def buildPadding(self, start, end):
        # Print padding
        left_padding = '' if not start else self.tab
        right_padding = '' if not end else self.tab
        return left_padding, right_padding

    def buildUnderline(self, error):
        # Error tokens
        start, err, end = error
        # Evaluate padding
        left_padding, right_padding = self.buildPadding(start, end)
        # Build padding
        left = ' ' * (len(start) + len(left_padding))
        right = ' ' * (len(end) + len(right_padding))
        # Build underline string
        return '{}{}{}'.format(left, '^' * len(err), right)

