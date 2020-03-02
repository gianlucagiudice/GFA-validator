# Regexp definition
orientationRegexp = '+|-'
nameRegexp = '[!-)+-<>-~][!-~]*'
cigarRegexp = '\*|(([0-9]+[MIDNSHPX=]),?)+'
sequenceRegexp = '\*|[A-Za-z=.]+'
integerRegexp = '[0-9]*'

# TODO: Remove unused fields
# Optional fields dictionary
optionalFieldsRegexp = {
    'A': '[!-~]',
    'i': '[-+]?[0-9]+',
    'f': '[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?',
    'Z': '[ !-~]+',
    'J': '[ !-~]+',
    'H': '[0-9A-F]+',
    'B': '[cCsSiIf](,[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)+'
}

# Optional fields
optionalFields = {
    'LN': (optionalFieldsRegexp['i'], 'Segment length'),
    'RC': (optionalFieldsRegexp['i'], 'Read count'),
    'FC': (optionalFieldsRegexp['i'], 'Fragment count'),
    'KC': (optionalFieldsRegexp['i'], 'k-mer count'),
    'SH': (optionalFieldsRegexp['H'], 'SHA-256 checksum of the sequence'),
    'UR': (optionalFieldsRegexp['Z'], 'URI or local file-system path of the sequence.'
                                      'If it does not start with a standard protocol (e.g. ftp), '
                                      'it is assumed to be a local path.'),
    'MQ': (optionalFieldsRegexp['i'], 'Mapping quality'),
    'NM': (optionalFieldsRegexp['i'], 'Number of mismatches/gaps'),
    'ID': (optionalFieldsRegexp['Z'], 'Edge identifier')
}

# Parsing dictionary
parsingDict = {
    # Comment
    '#': {'required': ('.*', 'Comment'),
          'optional': {}
          },
    # Segment
    'S': {'required': ((nameRegexp, 'Segment name'),
                       (sequenceRegexp, 'Optional nucleotide sequence')),
          'optional': {'LN': optionalFields['LN'],
                       'RC': optionalFields['RC'],
                       'FC': optionalFields['FC'],
                       'KC': optionalFields['KC'],
                       'SH': optionalFields['SH'],
                       'UR': optionalFields['UR']}
          },
    # Link
    'L': {'required': ((nameRegexp, 'Name of segment'),
                       (orientationRegexp, 'Orientation of From segment'),
                       (nameRegexp, 'Name of segment'),
                       (orientationRegexp, 'Orientation of To segment'),
                       (cigarRegexp, 'Optional CIGAR string describing overlap')),
          'optional': {'MQ': optionalFields['MQ'],
                       'NM': optionalFields['NM'],
                       'RC': optionalFields['RC'],
                       'FC': optionalFields['FC'],
                       'KC': optionalFields['KC'],
                       'ID': optionalFields['ID']}
          },
    # Containment
    'C': {'required': ((nameRegexp, 'Name of container segment'),
                       (orientationRegexp, 'Orientation of container segment'),
                       (nameRegexp, 'Name of contained segment'),
                       (orientationRegexp, 'Orientation of contained segment'),
                       (integerRegexp, '0-based start of contained segment'),
                       (cigarRegexp, 'CIGAR string describing overlap')),
          'optional': {'RC': optionalFields['RC'],
                       'NM': optionalFields['NM'],
                       'ID': optionalFields['ID']}
          },
    # Path
    'P': {'required': ((nameRegexp, 'Path name'),
                       (nameRegexp, 'A comma-separated list of segment names and orientations'),
                       (cigarRegexp, 'Optional comma-separated list of CIGAR strings')),
          'optional': {}
          }
}
