#! /opt/homebrew/bin/python3

def get_input():
    #Function to get the input number

    number = input("Enter the number: ")
    return number

def calculate_fib(number):
    #calculate fib number

    a, b = 0, 1
    for i in range(int(number)):
        a,b = b,a+b
    return a

def print_output(number, a):

    print('The Fibonacci number for', number, 'is', a)

def main():
    #main function

    number = get_input()
    a = calculate_fib(number)
    print_output(number, a)

if __name__ == "__main__":
    main()

