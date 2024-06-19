# Reverse cipher
msg = input("Input your message")
n = len(msg)
reverse_msg = ''
i = n-1
while (i>=0):
    reverse_msg = reverse_msg + msg[i]
    i = i-1
print("reverse cipher of messgae is:", reverse_msg)






















