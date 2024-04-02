#! /opt/homebrew/bin/python3

size = int(input("Enter the size of your table: "))

for i in range(1,size+1):
    for j in range(1,size+1):
        print(i * j, end=' ')
    print()
