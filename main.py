import sys
from parser.Config import PATH
from parser.Parser import Parser


def main():
    # Get file name
    file_name = parseArguments(sys.argv)
    # Read file
    lines = readFile(file_name)
    # Create parser object
    parser = Parser(lines)
    # Compute errors
    errors = [line.parsingError for line in parser.parse() if line.parsingError]
    # Print results
    if not errors:
        print("File is valid.")
    else:
        for error in errors:
            print(error, end='')
        print("File is not valid.")


def parseArguments(args):
    if len(args) != 2:
        print("ERROR: Invalid number of arguments.")
        quit(-1)
    return PATH + args[1]


def readFile(path):
    try:
        with open(path) as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print('ERROR: File "{}" not found in "{}"'.format(path.split('/')[-1], PATH))
        quit(-2)


if __name__ == '__main__':
    main()
