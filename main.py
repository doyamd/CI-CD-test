def fizzBuzz(num):
    if num%3 == 0 and num%5 == 0:
        return "FizzBuzz"
    elif num%3 == 0:
        return "Fizz"
    elif num%5 == 0:
        return "Buzz"

def main():
    num = int(input())
    print(fizzBuzz(num))
if __name__ == "__main__":
    main()