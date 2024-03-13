import cv2
import pytesseract
from pydantic import BaseModel

class TextData(BaseModel):
    text: str

def extract_text_from_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Preprocess the image (optional, depending on the quality of the image)
    # For example: convert to grayscale, apply thresholding, etc.
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use Tesseract to extract text from the image
    extracted_text = pytesseract.image_to_string(gray_image)
    
    return extracted_text

def count_characters_and_numbers(text):
    num_characters = len(text)
    num_numbers = sum(c.isdigit() for c in text)
    return num_characters, num_numbers

# Example usage
image_path = 'image_with_text.jpg'
extracted_text = extract_text_from_image(image_path)

# Validate the extracted text using Pydantic
text_data = TextData(text=extracted_text)

# Count characters and numbers
num_characters, num_numbers = count_characters_and_numbers(text_data.text)
print("Number of characters:", num_characters)
print("Number of numbers:", num_numbers)

