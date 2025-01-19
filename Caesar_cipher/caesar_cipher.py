message=input("Enter a message : ")
key=int(input("Enter key code : "))
ciphertext=""
for ch in message:
    ordinal_ch=ord(ch)
    ordinal_ch+=key
    if ordinal_ch > ord('z'):
        ordinal_ch=ord('a')+(ordinal_ch-ord('z'))
    new_ch=chr(ordinal_ch)
    ciphertext+=new_ch
print(ciphertext)


decrypted_message = ""

for ch in ciphertext:
    ordinal_ch = ord(ch)
    ordinal_ch -= key
    if ordinal_ch < ord('a'):
        ordinal_ch = ord('z') - (ord('a') - ordinal_ch - 1)
    new_ch = chr(ordinal_ch)
    decrypted_message += new_ch

print("Decrypted message:", decrypted_message)