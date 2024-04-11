# Michael Salemi Encode function

def encode(password):
    password = str(password)
    list_num = []
    encoded = ''
    for i in range(0, len(password)):
        list_num.append(int(password[i:i + 1]))
    for i in range(0, len(password)):
        if list_num[i] == 7:
            list_num[i] = 0
        elif list_num[i] == 8:
            list_num[i] = 1
        elif list_num[i] == 9:
            list_num[i] = 2
        else:
            list_num[i] = list_num[i] + 3
    for i in range(0, len(password)):
        encoded = encoded + str(list_num[i])
    print('Your password has been encoded and stored')
    print(encoded)
    return encoded

#Decode Function (Written by Juan)
def decode(password):
    decoded_password = ""
    for i in range(0, len(password)):
        decoded_password += str(((int(password[i]) + 10) - 3)%10)
    return decoded_password

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
                to_encode = str(to_encode)
                password = encode(to_encode)
                stored_password = password
            except ValueError:
                print('Please enter a valid password!')


        elif user_in == 2:
            #Print string (Modified by Juan)
            print(f"The encoded password is {stored_password}, and the original password is {decode(stored_password)}.")

        elif user_in == 3:
            running = False

        else:
            print("Please enter a valid input")

        print('')


if __name__ == '__main__':
    main()
