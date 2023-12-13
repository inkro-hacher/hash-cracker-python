#####################################################
#                    Import moduls
from urllib.request import hashlib
import sys
import pyfiglet
#                    Banner Hash cracker
ascii_banner = pyfiglet.figlet_format("Hash Cracker")
print(ascii_banner)
#                   Some Hash
print("Note! We are useing own wordlist, But don't panic,\n If you want to use your own wordlist, that facility is available.!")
# 1. MD5      Hash
# 2. SHA1     Hash
# 3. SHA224   Hash
# 4. SHA256   Hash
# 5. SHA384   Hash
# 6. SHA512   Hash
print()
while True:  # Start of while loop and all programing
    print("Enter Type of Hash to be cracked (Select blow option.!)\n \n 1 <-> MD5 Hash \n 2 <-> SHA1 Hash \n 3 <-> SHA224 Hash \n 4 <-> SHA256 Hash \n 5 <-> SHA384 Hash \n 6 <-> SHA512 Hash \n 7 <-> Quit Script")
    print()
    usr_hash = input("->")
    if (usr_hash == '1'):
        pssFound = False
        md5hash = input("Please insrt the MD5 hash to crack.?\n->")
        if (md5hash == ""):
            passFound = True
            print("Please enter md5 hashed.!")
            break
        print()
        usr_own = input("Did you give your wordlist.? (y/n) \n->")
        if usr_own == 'y':
            word_list = input("Please enter your wordlist location.?\n>")
            with open(word_list, "r") as file:
                for guess in file:
                    hashedguess = hashlib.md5(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == md5hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != md5hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Wordlist not found.!")
        elif usr_own == 'n':
            with open("inkro-wordlist.txt", "r") as file:
                for guess in file:
                    hashedguess = hashlib.md5(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == md5hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != md5hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Password not found in our wordlist, Try again with your own wordlist.?")
    elif (usr_hash == '2'):
        pssFound = False
        sha1hash = input("Please enter the SHA1 hash to crack.?\n->")
        if (sha1hash == ""):
            passFound = True
            print("Please enter sha1 hashed.!")
            break
        print()
        usr_own = input("Did you give your wordlist.? (y/n) \n->")
        if usr_own == 'y':
            word_list = input("Please enter your wordlist location.?\n->")
            with open(word_list, "r") as file:
                for guess in file:
                    hashedguess = hashlib.sha1(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == sha1hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != sha1hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Wordlist not found.!")
        elif usr_own == 'n':
            with open("inkro-wordlist.txt", "r") as file:
                for guess in file:
                    hashedguess = hashlib.sha1(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == sha1hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != sha1hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Password not found in our wordlist, Try again with your own wordlist.?")
    elif (usr_hash == '3'):
        pssFound = False
        sha224hash = input("Please enter the SHA224 hash to crack.?\n->")
        if (sha224hash == ""):
            passFound = True
            print("Please enter sha224 hashed.!")
            break
        print()
        usr_own = input("Did you give your own wordlist.? (y/n) \n->")
        if usr_own == 'y':
            word_list = input("Please enter your wordlist location.?\n->")
            with open(word_list, "r") as file:
                for guess in file:
                    hashedguess = hashlib.sha224(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == sha224hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != sha224hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Wordlist not found.!")
        elif usr_own == 'n':
            with open("inkro-wordlist.txt", "r") as file:
                for guess in file:
                    hashedguess = hashlib.sha224(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == sha224hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != sha224hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Password not found in our wordlist, Try again with your own wordlist.?")
    elif (usr_hash == '4'):
        pssFound = False
        sha256hash = input("Please enter the SHA256 hash to crack.?\n->")
        if (sha256hash == ""):
            passFound = True
            print("Please enter sha256 hashed.!")
            break
        print()
        usr_own = input("Did you give your own wordlist.? (y/n) \n->")
        if usr_own == 'y':
            word_list = input("Please enter your wordlist location.?\n->")
            with open(word_list, "r") as file:
                for guess in file:
                    hashedguess = hashlib.sha256(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == sha256hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != sha256hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Wordlist not found.!")
        elif usr_own == 'n':
            with open("inkro-wordlist.txt", "r") as file:
                for guess in file:
                    hashedguess = hashlib.sha256(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == sha256hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != sha256hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Password not found in our wordlist, Try again with your own wordlist.?")
    elif (usr_hash == '5'):
        pssFound = False
        sha384hash = input("Please enter the SHA384 hash to crack.?\n->")
        if (sha384hash == ""):
            passFound = True
            print("Please enter sha384 hashed.!")
            break
        print()
        usr_own = input("Did you give your own wordlist.? (y/n) \n->")
        if usr_own == 'y':
            word_list = input("Please enter your wordlist location.?\n->")
            with open(word_list, "r") as file:
                for guess in file:
                    hashedguess = hashlib.sha384(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == sha384hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != sha384hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Wordlist not found.!")
        elif usr_own == 'n':
            with open("inkro-wordlist.txt", "r") as file:
                for guess in file:
                    hashedguess = hashlib.sha384(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == sha384hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != sha384hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Password not found in our wordlist, Try again with your own wordlist.?")
    elif (usr_hash == '6'):
        pssFound = False
        sha512hash = input("Please enter the SHA512 hash to crack.?\n->")
        if (sha512hash == ""):
            passFound = True
            print("Please enter sha512 hashed.!")
            break
        print()
        usr_own = input("Did you give your own wordlist.? (y/n) \n->")
        if usr_own == 'y':
            word_list = input("Please enter your wordlist location.?\n->")
            with open(word_list, "r") as file:
                for guess in file:
                    hashedguess = hashlib.sha512(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == sha512hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != sha512hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Wordlist not found.!")
        elif usr_own == 'n':
            with open("inkro-wordlist.txt", "r") as file:
                for guess in file:
                    hashedguess = hashlib.sha512(bytes(guess.strip(), "utf-8")).hexdigest()
                    if hashedguess.upper() == sha512hash.upper():
                        print("The password is :-> ", str(guess))
                        passFound = True
                        break
                    elif hashedguess != sha512hash:
                        print("The password guess", str(guess),"does not match, Try again with a different wordlist.!" )
            if (passFound == False):
                print("Password not found in our wordlist, Try again with your own wordlist.?")
    elif usr_hash == '7':
        print("Thank you very much for using our Hash cracker.!!!")
        quit()
