from collections import deque


def is_palindrome(input: str) -> bool:

    if not isinstance(input, str):
        raise TypeError("Input must be a str")

    if input == "":
        raise ValueError("Input must not be an empty string")

    dq = deque()

    for chr in input:
        if chr != ' ':
            dq.append(chr.lower())

    while len(dq) > 1:
        l: str = dq.popleft()
        r: str = dq.pop()

        if l != r:
            return False
    return True


def main():

    def test(test_str):
        print(test_str, "|", is_palindrome(test_str))

    test("A")
    test("AA")
    test("ABA")
    test("ABBA")
    
    print("\n--- Cases ---")
    test("Aba")
    test("RaceCar")
    test("A man a plan a canal Panama")
    test("Madam")
    
    print("\n--- Spaces ---")
    test("taco cat")
    test("A Santa at NASA")
    test("Was it a car or a cat I saw")
    
    print("\n--- Not palindrome ---")
    test("HELLO")
    test("HEOEH")
    test("Python")
    test("AB")
    
    print("\n--- Special chars ---")
    test("A|||a")
    test("-+-")
    test("12321")
    test("12345")

    try:
        test("")
    except ValueError:
        print("Empty string")

if __name__ == "__main__":
    main()
