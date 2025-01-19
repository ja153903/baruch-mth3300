def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print(f"The sum of {a} and {b} is {add(a, b)}")
