def nameValidator(name):
    count = 0
    for var in name:
        if var == ' ':
            count += 1

    if count == 0 or count > 1:
        raise Exception('Enter only your first and last name')
    elif count != 1:
        raise Exception('Only one line space required')
    else:
        space = name.index(' ')
        first_name = name[0:space]
        last_name = name[space + 1:]
        if len(first_name) < 5 or len(first_name) > 20 or len(last_name) < 5 or len(last_name) > 20:
            raise Exception('Lengths of the character must be in between 5 and 20')
        else:
            print('Welcome!!!')


user_input = input('Enter your name (surname & first name): ')
nameValidator(user_input)

