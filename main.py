# Michael Salemi Encode function

def encode(password):
    password = str(password)
    list_num = []
    encoded = ''
    for i in range(0, len(password)):
        list_num.append(int(password[i:i + 1]) + 3)
    for i in range(0, len(password)):
        encoded = encoded + str(list_num[i])
    print('Your password has been encoded and stored')
    return encoded


def decode():
    pass


def main():
    running = True

    stored_password = ''

    while running:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')

        user_in = 0
        try:
            user_in = int(input('Please enter an option: '))
        except ValueError:
            pass

        if user_in == 1:
            to_encode = 0
            try:
                to_encode = int(input('Please enter your password to encode: '))
            except ValueError:
                print('Please enter a valid password!')

            to_encode = str(to_encode)
            password = encode(to_encode)
            stored_password = password

        elif user_in == 2:
            decode()

        elif user_in == 3:
            running = False

        else:
            print("Please enter a valid input")

        print('')


if __name__ == '__main__':
    main()
