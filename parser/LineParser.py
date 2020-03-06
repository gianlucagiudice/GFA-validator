import re

from parser.ParsingError import ParsingError


class LineParser:
    def __init__(self, line_number, line):
        # Number of line in file
        self.lineNumber = line_number
        # Content of line
        self.line = line
        # Set of optional fields occurrence
        self.optionalFieldsSet = set()
        # Parsing error
        self.parsingError = None

    def parse(self, parsing_dict):
        # Skip blank line
        if len(self.line) == 0:
            return self
        # Extract tag and tokens
        tag, *tokens = self.line.split('\t')
        # Check if tag is valid
        if tag not in parsing_dict.keys():
            self.buildError([], tag, tokens, 'record type')
            return self
        # Parse required fields
        self.parseRequiredFields(tag, tokens, parsing_dict)
        # Check if line is valid so far
        if self.parsingError is None:
            # Parse optional fields
            self.parseOptionalFields(tag, tokens, parsing_dict)
        # Return parsed line
        return self

    def parseRequiredFields(self, tag, tokens, parsing_dict):
        required_fields_list = parsing_dict[tag]['required']
        # Check if all required fields are present
        if len(tokens) < len(required_fields_list):
            self.buildError([], [tag] + tokens, [], 'number of fields for tag "{}"'.format(tag))
        else:
            # Parse required fields
            for index, (token, (regexp, description)) in enumerate(zip(tokens, required_fields_list)):
                if not re.match(regexp, token):
                    # Invalid token
                    self.buildError([tag] + tokens[:index], token, tokens[index + 1:], description)

    def parseOptionalFields(self, tag, tokens, parsing_dict):
        # Get all fields
        optional_fields_dict = parsing_dict[tag]['optional']
        offset = len(parsing_dict[tag]['required'])
        optional_fields = tokens[offset:]
        # Parse all optional fields
        for index, optional_field in enumerate(optional_fields):
            # Build error position
            err_start = [tag] + tokens[:offset + index]
            err_end = tokens[offset + index + 1:]
            # Check if optional filed format is valid
            if not self.isValidFormat(optional_field, err_start, err_end):
                return
            # Tokenize optional field
            opt_tag, opt_type, value = optional_field.split(':')
            # Check if optional tag is valid for target line tag
            if not self.isValidTag(tag, opt_tag, optional_field, optional_fields_dict, err_start, err_end):
                return
            # Check if optional tag is unique in line
            if not self.isValidOccurrence(opt_tag, optional_field, err_start, err_end):
                return
            # Check if optional field type is valid
            target_type, regexp, err_description = optional_fields_dict[opt_tag]
            if not self.isValidType(opt_type, target_type, opt_tag, optional_field, err_start, err_end):
                return
            # Check if field matches regexp
            if not self.isValidMatch(regexp, value, optional_field, err_description, err_start, err_end):
                return

    def isValidFormat(self, optional_field, err_start, err_end):
        if len(optional_field.split(':')) != 3:
            err_description = 'optional field format'
            self.buildError(err_start, optional_field, err_end, err_description)
        return not self.parsingError

    def isValidTag(self, tag, opt_tag, optional_field, optional_fields_dict, err_start, err_end):
        if opt_tag not in optional_fields_dict.keys():
            err_description = 'optional tag {}, for record type {}'.format(opt_tag, tag)
            self.buildError(err_start, optional_field, err_end, err_description)
        return not self.parsingError

    def isValidOccurrence(self, opt_tag, optional_field, err_start, err_end):
        if opt_tag in self.optionalFieldsSet:
            err_description = 'occurrence of optional tag {}. Field is not unique'.format(opt_tag)
            self.buildError(err_start, optional_field, err_end, err_description)
        self.optionalFieldsSet.add(opt_tag)
        return not self.parsingError

    def isValidType(self, opt_type, target_type, opt_tag, optional_field, err_start, err_end):
        if not opt_type == target_type:
            err_description = 'type for optional field {}'.format(opt_tag)
            self.buildError(err_start, optional_field, err_end, err_description)
        return not self.parsingError

    def isValidMatch(self, regexp, value, optional_field, err_description, err_start, err_end):
        if not re.match(regexp, value):
            self.buildError(err_start, optional_field, err_end, err_description)
        return not self.parsingError

    def buildError(self, start, error, end, description):
        error = error if type(error) is list else [error]
        self.parsingError = ParsingError(start, error, end, description, self.lineNumber)
