def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_message += chr(shifted)
        else:
            decrypted_message += char
    return decrypted_message

message = "Hello, World!"
shift = 3
encrypted = encrypt(message, shift)
print("encrypted message:", encrypted)
decrypted = decrypt(encrypted, shift)
print("decrypted message:", decrypted)