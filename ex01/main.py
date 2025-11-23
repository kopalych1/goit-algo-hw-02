from collections import deque


def is_palindrome(input: str) -> bool:

    if not isinstance(input, str):
        raise TypeError("Input must be a str")

    if input == "":
        raise ValueError("Input must not be an empty string")

    dq = deque()

    for chr in input:
        dq.append(chr)

    for _ in range(len(dq) // 2):
        l: str = dq.popleft()
        r: str = dq.pop()

        if l != r:
            return False
    return True


def main():

    def test(test_str):
        print(test_str, "|", is_palindrome(test_str))

    test("HELLO")
    test("HEOEH")
    test("CARRAC")
    test("OK")
    test("-+-")
    test("AA")
    test("A")
    try:
        test("")
    except ValueError:
        print("Empty string")

if __name__ == "__main__":
    main()
