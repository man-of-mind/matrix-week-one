def dictComp(stop, step):
    valid = int(stop / step)
    new_dict = {'items-{}'.format(n):0 for n in range(1, valid + 1)}
    numbers = list(range(1, stop + 1))
    print(numbers)
    value = [numbers[x:x + step] for x in range(0, stop + 1, step) if x < len(numbers) - 1]
    for val in value:
        if len(val) < step:
            value.remove(val)
    num_dict = dict(zip(new_dict, value))
    print(num_dict)


last = int(input('Enter the ending number: '))
stepping = int(input('Enter the step: '))
dictComp(last, stepping)