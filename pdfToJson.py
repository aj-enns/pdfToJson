import PyPDF2
import json
import os
import logging

# Configure logging
logging.basicConfig(filename='pdfToJson.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def pdf_to_json(pdf_file_path, json_file_path):
    try:
        # Open the PDF file in binary mode
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Initialize an empty list to store the extracted text
            pdf_text = []

            # Loop through each page in the PDF and extract text
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                pdf_text.append(page_text)

            # Create a dictionary to store the PDF text
            pdf_data = {"text": pdf_text}

            # Convert the dictionary to JSON and save it to a file
            with open(json_file_path, "w") as json_file:
                json.dump(pdf_data, json_file, indent=4)

        logging.info(f"PDF text has been successfully converted to JSON and saved to {json_file_path}")
    except FileNotFoundError as e:
        logging.error(f"File not found: {str(e)}")
    except PermissionError as e:
        logging.error(f"Permission error: {str(e)}")
    except PyPDF2.utils.PdfReadError as e:
        logging.error(f"PDF read error: {str(e)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

# Usage example:
current_dir = os.path.dirname(__file__)
pdf_file_path = os.path.join(current_dir, "input.pdf") # Replace with your PDF file path
json_file_path = os.path.join(current_dir, "output.json") # Replace with your desired JSON file path

pdf_to_json(pdf_file_path, json_file_path)
