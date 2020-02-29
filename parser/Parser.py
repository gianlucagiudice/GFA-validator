# Regexp
stringType1 = '+|-'
stringType2 = '[!-)+-<>-~][!-~]*'
stringType3 = '\*|(([0-9]+[MIDNSHPX=]),?)+'
stringType4 = '\*|[A-Za-z=.]+'
integer = '[0-9]*'

# Optional fields dictionary
optionalFieldsDict = {
    'A': ('[!-~]', 'Printable character'),
    'i': ('[-+]?[0-9]+', 'Signed integer'),
    'f': ('[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?', 'Single-precision floating number'),
    'Z': ('[ !-~]+', 'Printable string, including space'),
    'J': ('[ !-~]+', 'JSON, excluding new-line and tab characters'),
    'H': ('[0-9A-F]+', 'Byte array in hex format'),
    'B': ('[cCsSiIf](,[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)+', 'Array of integers or floats')
}
# Parsing dictionary
parsingDict = {
    # Comment line
    '#': {'required': '.*',
          'optional': {}},
    # Segment line
    'S': {'required': ((stringType2, 'Segment name'),
                       (stringType4, 'Optional nucleotide sequence')),
          'optional': {'LN': optionalFieldsDict['i'],
                       'RC': optionalFieldsDict['i'],
                       'FC': optionalFieldsDict['i'],
                       'KC': optionalFieldsDict['i'],
                       'SH': optionalFieldsDict['H'],
                       'UR': optionalFieldsDict['Z']}}
    # Link line

}


class Parser:
    def __init__(self, lines):
        self.lines = lines
        self.parsingDict = parsingDict

    def parse(self):
        # Header is optional
        self.parseHeader()
        # Parse rest of file
        return

    def parseHeader(self):
        # ... header
        return
