def is_symmetrical(input: str) -> bool:

    if not isinstance(input, str):
        raise TypeError("Input must be a str")

    if input == "":
        raise ValueError("Input must not be an empty string")

    stack = list()

    for chr in input:
        if not chr in "(){}[]":
            continue

        if chr in "({[":
            stack.append(chr)

        if chr in ")}]":
            if len(stack) == 0:
                return False

            top: str = stack.pop()

            if ({'(': ')', '{': '}', '[': ']'}[top] != chr):
                return False

    return True



def main():

    def test(test_str):
        print(test_str, "|", is_symmetrical(test_str))

    test("{}{}()")
    test("{}")
    test("[)")
    test("[[)]")
    test("([{}][]{})")
    try:
        test("")
    except ValueError:
        print("Empty string")

if __name__ == "__main__":
    main()
