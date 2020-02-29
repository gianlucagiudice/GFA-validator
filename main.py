from parser.Parser import Parser
from parser.Config import FILE_PATH


def main():
    # Read file
    lines = readFile(FILE_PATH)
    # Create parser object
    parser = Parser(lines)
    # Parse each line
    parsed_lines = parser.parse()
    # Filter valid lines
    #invalid_lines = validated_lines
    # Print results

def readFile(path):
    with open(path) as file:
        return [tweet.strip() for tweet in file.readlines()]


if __name__ == '__main__':
    main()
