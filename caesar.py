def shift(letter, shift_amount):
    unicode = ord(letter) + shift_amount

    if (unicode > 127):
        unicode = unicode - 95
    elif (unicode < 32):
        unicode += 95

    new_letter = chr(unicode)
        
    return new_letter

def encrypt(message, shift_amount):
    result = ""

    for letter in message:
        result += shift(letter , shift_amount)

    return result

def decrypt(message, shift_amount):
    return encrypt(message, -(shift_amount))


unencrypted_message = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little."
encrypted_message = encrypt(unencrypted_message, 5)
decrypted_message = decrypt(encrypted_message, 5)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)
