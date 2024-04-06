#encrypt/decrypt text Caesar Cipher algorithm
#user input a message
#input shift value
#encrypt/decrypt

def encrypt(msg, n):
    e_msg=""
    length=len(msg)
    for i in range(length):
        ch=msg[i]
        if ch==" ":
            e_msg+=" "
        elif(ch.isupper()):
            val=ord(ch) + n - 65
            e_msg+=chr( val % 26 + 65)
        elif(ch.islower()):
            val=ord(ch) + n - 97
            e_msg+=chr(val % 26 + 97)
    print("\n"+"Encrypted text: "+e_msg+"\n")

def decrypt(msg, n):
    e_msg=""
    length=len(msg)
    for i in range(length):
        ch=msg[i]
        if ch==" ":
            e_msg+=" "
        elif(ch.isupper()):
            val=ord(ch) - n - 65
            e_msg+=chr( val % 26 + 65)
        elif(ch.islower()):
            val=ord(ch) - n - 97
            e_msg+=chr(val % 26 + 97)
    print("\n"+"Decrypted text: "+e_msg+"\n")

def main():
    str=input("enter text: ")
    n=int(input("enter shift value : "))
    while True:
        print("\n1.Encrypt")
        print("\n2.Decrypt")
        print("\n3.Exit")
        ch=int(input("enter your choice: "))
        if ch==1:
            encrypt(str,n)
        elif ch==2:
            decrypt(str,n)
        elif ch==3:
            break
        else:
            print("\nwrong choice")


if __name__=="__main__":
    main()