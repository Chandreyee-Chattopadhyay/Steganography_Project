import encrypt
import decrypt

image_path = "Stegnography_project/pic.jpg"  # Make sure this image exists

# Encryption
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Encrypt and get password + message length
stored_password, msg_length = encrypt.encrypt_message(image_path, msg, password)

if stored_password is None:
    print("Encryption failed. Exiting.")
    exit()

# Decryption
user_password = input("Enter passcode for decryption: ")
decrypt.decrypt_message("encryptedImage.png", msg_length, stored_password, user_password)
