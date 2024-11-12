import difflib
from time import time as t
import cv2
import easyocr
import numpy as np
import pyautogui as pg
from PIL import ImageGrab
import os

# Define the model storage directory
model_storage_directory = "C:\\Users\\USER\\Documents\\chatbot\\New folder\\.EasyOCR\\model"

# Ensure the model storage directory exists
os.makedirs(model_storage_directory, exist_ok=True)

# Initialize EasyOCR Reader without downloading models
reader = easyocr.Reader(['en'], gpu=False, model_storage_directory=model_storage_directory, download_enabled=False)

def center(points):
    """Calculate the center of the bounding box."""
    sum_x = sum(point[0] for point in points)
    sum_y = sum(point[1] for point in points)
    center_x = sum_x / len(points)
    center_y = sum_y / len(points)
    return int(center_x), int(center_y)

def Ocr(st, double_click=False):
    """Perform OCR on the screen and click the closest match to the given string."""
    # Capture the screen
    screen = np.array(ImageGrab.grab())
    image_np = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    # Perform OCR
    c = t()
    result = reader.readtext(image_np)
    print("Read in", t() - c, "seconds.")

    # Find the closest match
    arr_of_words = [i[1].lower() for i in result]
    closest_match = difflib.get_close_matches(st.lower(), arr_of_words, n=1)

    if closest_match:
        for i in result:
            if i[1].lower() == closest_match[0].lower():
                print(i[0])  # Print the bounding box coordinates
                # Click the center of the matched text
                if double_click:
                    pg.click(center(i[0]))
                    pg.sleep(0.35)
                    pg.click(center(i[0]))
                else:
                    pg.click(center(i[0]))
                break

        return "Clicked '" + st + "' button."

    else:
        return f"No button found named '{st}'."

# # Test the function
# print(Ocr("Google"))
