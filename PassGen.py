import random
import time
import sys
import os
import base64
import string
import webbrowser


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*?;'

number = input('How Many Passwords Do You Want?: ')
number = int(number)

length = input('Length Of The Password: ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)

exit_program = input('Want To Go To The OutPut File / Password Encryptor? (Y/N): ')

if exit_program == 'N':
    KeyboardInterrupt
elif exit_program == 'n':
    KeyboardInterrupt
elif exit_program == 'Y':
    time.sleep(2)
elif exit_program == 'y':
    time.sleep(2)

    def write_file(path, text):
        file_write = open(path, "w")
        file_write.write(text)
        file_write.close()

    print('''
        d8888b.   j88D  .d8888. .d8888.  d888b  d8888b. d8b   db 
        88  `8D  j8~88  88'  YP 88'  YP 88' Y8b VP  `8D 888o  88 
        88oodD' j8' 88  `8bo.   `8bo.   88        oooY' 88V8o 88 
        88~~~   V88888D   `Y8b.   `Y8b. 88  ooo   ~~~b. 88 V8o88 
        88          88  db   8D db   8D 88. ~8~ db   8D 88  V888 
        88          VP  `8888Y' `8888Y'  Y888P  Y8888P' VP   V8P ''')

    print('''
        [1] Encrypt Password
        [2] Out Put Password Into Document
        [3] My GitHub
        ''')
    print('\n')

    pass_gen = input('P4SSG3N~# ')
    
    if pass_gen == '3':
        url = f'https://github.com/MalwareMix'
        webbrowser.get().open(url)
    elif pass_gen == '2':
        user_input = input('Enter Your Password: ')
        write_file('OutPut.txt', user_input)
    elif pass_gen == '1':
        print('Enter The String You Want To Encode Into Bas64!')
        string = input('STRING: ')
        sample_string = string
        sample_string_bytes = sample_string.encode("ascii")

        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        print(f"H3R3 T4K3 TH1S!: {base64_string}")
        print('Out Put To A .txt File?')
        UwU = input('(Y/N): ')
        if UwU == 'Y':
            write_file('Encrypted.txt', base64_string)
        elif UwU == 'y':
            write_file('Encrypted.txt', base64_string)
        elif UwU == 'N':
            KeyboardInterrupt
        elif UwU == 'n':
            KeyboardInterrupt