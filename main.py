from parser.Config import FILE_PATH
from parser.Parser import Parser


def main():
    # Read file
    lines = readFile(FILE_PATH)
    # Create parser object
    parser = Parser(lines)
    # Compute errors
    errors = [line.parsingError for line in parser.parse() if line.parsingError]
    # Print results
    if not errors:
        print("File is valid.")
    else:
        [print(error, end='') for error in errors]
        print("\nFile is not valid.")


def readFile(path):
    with open(path) as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    main()
