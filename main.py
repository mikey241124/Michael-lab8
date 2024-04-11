#Michael Salemi's Encode function

def encode(password):
    to_encode = 0
    run = False
    try:
        to_encode = int(input('Please enter your password to encode: '))
        run = True
    except ValueError:
        print('Please enter a valid password!')

    if run:
        password = str(password)
        list = []
        for i in range(0, len(to_encode)):
            list.append(int(password[i:i+1]) + 3)




def decode():
    pass

def main():
    running = True
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
            encode()

        if user_in == 2:
            decode()

        if user_in == 3:
            running = False

        else:
            print("Please enter a valid input")

if __name__ == '__main__':
    main()