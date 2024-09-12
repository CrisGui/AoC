from functools import reduce


def get_input() -> str:
    with open("./input.txt", "r") as f:
        return f.read()


def main():
    input = get_input().split()
    output = []
    numbers = []

    for line in input:
        numbers += [list(filter(lambda x: x.isdigit(), line))]

    # print(numbers)

    for line in numbers:
        print(line)
        print(line[0] + line[-1])
        output += [line[0] + line[-1]]

    # print(output)

    print(reduce(lambda x, y: int(x) + int(y), output))


if __name__ == "__main__":
    main()
