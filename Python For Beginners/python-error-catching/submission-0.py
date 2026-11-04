def divide_numbers(a: str, b: str) -> None:
    try:
        x = int(a) / int(b)
        print(x)
    except Exception as e:
        print("An error occurred:", e)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
