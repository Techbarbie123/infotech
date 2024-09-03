def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char)
            if char.islower():
                encrypted_char = chr((char_code - 97 + shift_amount) % 26 + 97)
            else:
                encrypted_char = chr((char_code - 65 + shift_amount) % 26 + 65)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char)
            if char.islower():
                decrypted_char = chr((char_code - 97 - shift_amount) % 26 + 97)
            else:
                decrypted_char = chr((char_code - 65 - shift_amount) % 26 + 65)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# User input
plain_text = input("Enter the plain text: ")
shift_key = int(input("Enter the key: "))

# Encrypting the plain text
encrypted_text = encrypt(plain_text, shift_key)
print(f"Encrypted Text: {encrypted_text}")

# Decrypting the encrypted text
decrypted_text = decrypt(encrypted_text, shift_key)
print(f"Decrypted Text: {decrypted_text}")