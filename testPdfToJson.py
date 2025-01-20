import os
import json
import pytest
from pdfToJson import pdf_to_json

def test_pdf_to_json(tmp_path):
    """
    Test the pdf_to_json function.

    This test verifies that the pdf_to_json function correctly converts a PDF file to a JSON file.
    It checks if the JSON file is created, and verifies its content to ensure the extracted text is as expected.

    Args:
        tmp_path (pathlib.Path): A temporary directory provided by pytest for storing the output JSON file.

    Returns:
        None
    """
    # Define the path for the input PDF file
    current_dir = os.path.dirname(__file__)
    pdf_file_path = os.path.join(current_dir, "input.pdf")

    # Define the path for the output JSON file
    json_file_path = tmp_path / "testOutput.json"

    # Call the function to convert PDF to JSON
    pdf_to_json(pdf_file_path, json_file_path)

    # Check if the JSON file was created
    assert os.path.exists(json_file_path)

    # Load the JSON file and verify its content
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
        assert "text" in data
        assert len(data["text"]) > 0
        assert "Hello, World!" in data["text"][0]

if __name__ == "__main__":
    pytest.main()
