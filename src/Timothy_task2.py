def oddNumbers(start, stop):
    return [x for x in range(start, stop + 1) if x % 2 != 0]


first = int(input('Enter the starting number: '))
end = int(input('Enter the last number: '))
print(oddNumbers(first, end))
