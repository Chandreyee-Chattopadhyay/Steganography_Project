import cv2
import numpy as np
import os

def encrypt_message(image_path, msg, password, output_image="encryptedImage.png"):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Unable to load image.")
        return None, None

    # Ensure the image is in RGB format
    if len(img.shape) < 3:
        print("Error: Image must be in RGB format.")
        return None, None

    d = {chr(i): i for i in range(255)}  # ASCII Mapping

    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]  # Store ASCII value in pixels
        z = (z + 1) % 3  # Switch between RGB channels

        # Move to next pixel
        if z == 0:
            m += 1
            if m >= img.shape[1]:  # Move to next row if width exceeds
                m = 0
                n += 1
                if n >= img.shape[0]:  # Prevent exceeding image size
                    print("Error: Message too long for this image!")
                    return None, None

    cv2.imwrite(output_image, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Save as PNG
    print(f"Encryption complete! Image saved as {output_image}")
    return password, len(msg)  # Return password and message length
