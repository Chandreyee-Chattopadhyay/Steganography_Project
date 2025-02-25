import cv2
import numpy as np

def decrypt_message(image_path, msg_length, stored_password, user_password):
    if stored_password != user_password:
        print("YOU ARE NOT AUTHORIZED!")
        return

    img = cv2.imread(image_path)

    if img is None:
        print("Error: Unable to load image.")
        return

    c = {i: chr(i) for i in range(255)}  # Reverse ASCII mapping

    message = ""
    n, m, z = 0, 0, 0

    for _ in range(msg_length):
        message += c[int(img[n, m, z])]  # Retrieve ASCII value and convert
        z = (z + 1) % 3  # Switch between RGB channels

        # Move to next pixel
        if z == 0:
            m += 1
            if m >= img.shape[1]:  # Move to next row if width exceeds
                m = 0
                n += 1
                if n >= img.shape[0]:  # Prevent exceeding image size
                    print("Error: Reached end of image during decryption!")
                    return

    print("Decrypted message:", message)
