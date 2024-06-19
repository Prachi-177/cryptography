# Caesar cipher
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# define a function that checks if input message contains alphabets only
def contains_only_alphabets(input_str):
    for char in input_str:
        if not char.isalpha():
            return False
        return True

#define plaintext containing only alphabets
while True:
    try:
        msg= input("input message:")

        #checking if input string contains alphabets only:dines
        if contains_only_alphabets(msg):
            break
        else:
            print("Input message does not contain alphabets only!!.")
    except ValueError:
        print("Input is not an alphabetic. Try again!!!")

#input a positive integer (between 1 to 26) as key (shift)
while True:
    try:
        key = int(input("enter a number between 1 and 26:"))
        if 1<=key<=26:
            break    #exit the loop if the input is valid
        else:
            print("Input is not between 1 and 26.  try again.")
    except ValueError:
        print("Input is not an integer. Try again.")

def caesar_encryption(text, shift):
    encrypted_text=''
    #changing text to upper (or lower) case
    text= text.upper()
    
    #length of text
    n =  len(text) 
    #encrypt text
    for i in range(n):
        c=text[i]
        loc=alpha.find(c)
        newloc=(loc + shift) % 26
        encrypted_text += alpha[newloc]
    return encrypted_text

def caesar_decryption(encrypted_text, shift):
    decrypted_text=''
    #changing text to upper (or lower) case
    text= encrypted_text.upper()
    #length of text
    
    #decrypt text
    for c in text:
        loc=alpha.find(c)
        newloc=(loc - shift) % 26
        decrypted_text += alpha[newloc]
    return decrypted_text

ciphertext = caesar_encryption(msg,key)
decrypted_text=caesar_decryption(ciphertext, key)
print("Plaintext:",msg)
print("Shift key:",key)
print("Ciphertext:",ciphertext)
print("Decrypted text:",decrypted_text)