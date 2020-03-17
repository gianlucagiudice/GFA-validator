# Regexp definition
orientationRegexp = '^((\+)|(-))$'
nameRegexp = '^[!-)+-<>-~][!-~]*$'
cigarRegexp = '^\*|(([0-9]+[MIDNSHPX=]),?)+$'
sequenceRegexp = '^(([ACTG]*)|(\*))$'
integerRegexp = '^[0-9]*$'

# Optional fields dictionary
optionalFieldsRegexp = {
    'i': '^[-+]?[0-9]+$',
    'Z': '^[ !-~]+$',
    'H': '^[0-9A-F]+$',
}

# Optional fields -> GFA format is (tag:type:value) [RC:i:51170]
optionalFields = {
    'LN': ('i', optionalFieldsRegexp['i'], 'Segment length'),
    'RC': ('i', optionalFieldsRegexp['i'], 'Read count'),
    'FC': ('i', optionalFieldsRegexp['i'], 'Fragment count'),
    'KC': ('i', optionalFieldsRegexp['i'], 'k-mer count'),
    'SH': ('H', optionalFieldsRegexp['H'], 'SHA-256 checksum of the sequence'),
    'UR': ('Z', optionalFieldsRegexp['Z'], 'URI or local file-system path of the sequence. '
                                           'If it does not start with a standard protocol '
                                           '(e.g. ftp), it is assumed to be a local path.'),
    'MQ': ('i', optionalFieldsRegexp['i'], 'Mapping quality'),
    'NM': ('i', optionalFieldsRegexp['i'], 'Number of mismatches/gaps'),
    'ID': ('Z', optionalFieldsRegexp['Z'], 'Edge identifier')
}

# Parsing dictionary
parsingDict = {
    # Comment
    '#': {'required': [('.*', 'Comment')],
          'optional': {}
          },
    # Segment
    'S': {'required': [(nameRegexp, 'Name of segment'),
                       (sequenceRegexp, 'Optional nucleotide sequence')],
          'optional': {'LN': optionalFields['LN'],
                       'RC': optionalFields['RC'],
                       'FC': optionalFields['FC'],
                       'KC': optionalFields['KC'],
                       'SH': optionalFields['SH'],
                       'UR': optionalFields['UR']}
          },
    # Link
    'L': {'required': [(nameRegexp, 'Name of segment'),
                       (orientationRegexp, 'Orientation of From segment'),
                       (nameRegexp, 'Name of segment'),
                       (orientationRegexp, 'Orientation of To segment'),
                       (cigarRegexp, 'Optional CIGAR string describing overlap')],
          'optional': {'MQ': optionalFields['MQ'],
                       'NM': optionalFields['NM'],
                       'RC': optionalFields['RC'],
                       'FC': optionalFields['FC'],
                       'KC': optionalFields['KC'],
                       'ID': optionalFields['ID']}
          },
    # Containment
    'C': {'required': [(nameRegexp, 'Name of container segment'),
                       (orientationRegexp, 'Orientation of container segment'),
                       (nameRegexp, 'Name of contained segment'),
                       (orientationRegexp, 'Orientation of contained segment'),
                       (integerRegexp, '0-based start of contained segment'),
                       (cigarRegexp, 'CIGAR string describing overlap')],
          'optional': {'RC': optionalFields['RC'],
                       'NM': optionalFields['NM'],
                       'ID': optionalFields['ID']}
          },
    # Path
    'P': {'required': [(nameRegexp, 'Path name'),
                       (nameRegexp, 'A comma-separated list of segment names and orientations'),
                       (cigarRegexp, 'Optional comma-separated list of CIGAR strings')],
          'optional': {}
          }
}
