import base64
import pyAesCryptModified
import random
from os import remove
from tqdm import tqdm
import argparse
from time import sleep
import pyfiglet




bufferSize = 128 * 1024

# encrypt
def remove_file(filename, level=100):
    for i in tqdm(range(level)):
        with open(filename, 'wb') as file:
            file.write(random.randbytes(10000000))
            file.close()
    remove(file)

def base64_encode(password):
    if isinstance(password, str):
        password = password.encode()
    old_password = base64.b64encode(password)
    for _ in tqdm(range(50)):
        new_password = base64.b64encode(old_password)
        old_password = new_password
    print(f'[INFO] {old_password.decode()}')
    return old_password.decode()
    

def encrypt_aes(password, filename, delete_original_file=False):
    pyAesCryptModified.encryptFile(filename, f"{filename}_encrypted.aes", password, bufferSize=bufferSize)
    if delete_original_file == True:
        remove_file(filename)


def decrypt_aes(password, filename, out_filename):
    pyAesCryptModified.decryptFile(filename, out_filename, password, bufferSize=bufferSize)


def main():
    art = pyfiglet.figlet_format("SUPER ENCODE", font="slant")
    print(art, end='\n\n\n\n\n\n\n')                                                   
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--filename", type=str, help="Имя файла")
    parser.add_argument("--password", type=str, help="Пароль")
    parser.add_argument("--mode", type=str, help="Режим encrypt или decrypt")
    parser.add_argument("--out", type=str, help="Файл куда сохронится результат")

    args = parser.parse_args()

    passwd = base64_encode(args.password)

    if args.mode == 'encrypt':
        encrypt_aes(
            filename=args.filename,
            password=passwd
        )
    elif args.mode == 'decrypt':
        decrypt_aes(
            filename=args.filename,
            password=passwd,
            out_filename=args.out
        )
    
        

if __name__ == '__main__':
    main()
