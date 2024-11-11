import openai
import base64
import json
from PIL import Image
from io import BytesIO
import pandas as pd
import os
from config import OPENAI_API_KEY

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

def extract_customer_info(image_path):
    # Step 1: Load and encode the image
    with Image.open(image_path) as img:
        # Convert image to RGB if it's not
        if img.mode != "RGB":
            img = img.convert("RGB")
        
        # Convert image to base64
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

    # Step 2: Create the message with the image
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "Extract customer information from this image and return ONLY a valid JSON object with this exact structure:\n"
                           "{\n"
                           "        \"Name\": \"\",\n"
                           "        \"Phone Number\": \"\",\n"
                           "        \"Mobile Number\": \"\",\n"
                           "        \"Email\": \"\",\n"
                           "        \"Street\": \"\",\n"
                           "        \"Street Number\": \"\",\n"
                           "        \"City\": \"\",\n"
                           "        \"ZIP Code\": \"\",\n"
                           "        \"State\": \"\",\n"
                           "        \"Country\": \"\",\n"
                           "        \"Latitude\": \"\",\n"
                           "        \"Longitude\": \"\"\n"
                           "}"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_str}"
                        # "detail": "low"
                    },
                    
                }
            ]
        }
    ]

    # Step 3: Send the image to OpenAI's Vision model
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=1000
    )

    # Step 4: Extract and process the response
    customer_info_text = response['choices'][0]['message']['content'].strip()
    print(f"Extracted Customer Information from {image_path}:\n", customer_info_text)

    try:
        # Try to clean the response if it contains additional text
        if customer_info_text.startswith("{") and customer_info_text.endswith("}"):
            json_str = customer_info_text
        else:
            # Try to find JSON object between curly braces
            start = customer_info_text.find("{")
            end = customer_info_text.rfind("}") + 1
            if start != -1 and end != 0:
                json_str = customer_info_text[start:end]
            else:
                raise json.JSONDecodeError("No valid JSON found", customer_info_text, 0)
        
        # Convert text to JSON
        customer_info = json.loads(json_str)
        return customer_info
        
    except json.JSONDecodeError as e:
        print(f"Could not convert to JSON. Error: {str(e)}")
        print("Raw response:", customer_info_text)
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def process_image_folder(folder_path):
    # Get all image files from the folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    all_customer_info = []
    
    # Process each image
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        customer_info = extract_customer_info(image_path)
        
        if customer_info:
            all_customer_info.append(customer_info)
    
    try:
        # Create DataFrame with all information
        df = pd.DataFrame(all_customer_info)
        
        # Save to Excel
        df.to_excel('customer_info.xlsx', index=False)
        print("\nExcel file 'customer_info.xlsx' has been created successfully!")
        
    except Exception as e:
        print(f"An error occurred while creating the Excel file: {str(e)}")

# Path to your image folder
folder_path = "images"  # Change this to your folder path
process_image_folder(folder_path)