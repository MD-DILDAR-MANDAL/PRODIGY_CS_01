#encrypt/decrypt text Caesar Cipher algorithm
#user input a message
#input shift value
#encrypt/decrypt

def encrypt():
    msg=input("enter text: ")
    n=int(input("enter shift value : "))
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

def decrypt():
    msg=input("enter text: ")
    n=int(input("enter shift value : "))
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
    
    while True:
        print("\n1.Encrypt")
        print("\n2.Decrypt")
        print("\n3.Exit")
        ch=int(input("enter your choice: "))
        if ch==1:
            encrypt()
        elif ch==2:
            decrypt()
        elif ch==3:
            break
        else:
            print("\nwrong choice")


if __name__=="__main__":
    main()