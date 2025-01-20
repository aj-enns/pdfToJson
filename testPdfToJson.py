import unittest
import os
import json
from unittest.mock import patch, mock_open, MagicMock
from pdfToJson import pdf_to_json
import io
import sys

class TestPdfToJson(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="fake pdf data")
    @patch("PyPDF2.PdfReader")
    def test_pdf_to_json_success(self, mock_pdf_reader, mock_open):
        # Mock the PDF reader and its methods
        mock_pdf = MagicMock()
        mock_pdf.pages = [MagicMock(), MagicMock()]
        mock_pdf.pages[0].extract_text.return_value = "Page 1 text"
        mock_pdf.pages[1].extract_text.return_value = "Page 2 text"
        mock_pdf_reader.return_value = mock_pdf

        # Define file paths
        current_dir = os.path.dirname(__file__)
        pdf_file_path = os.path.join(current_dir, "input.pdf")
        json_file_path = os.path.join(current_dir, "output.json")

        # Call the function
        pdf_to_json(pdf_file_path, json_file_path)

        # Check if the JSON file was written correctly
        mock_open.assert_called_with(json_file_path, "w")
        handle = mock_open()
        written_data = "".join(call.args[0] for call in handle.write.call_args_list)
        json_data = json.loads(written_data)
        self.assertEqual(json_data, {"text": ["Page 1 text", "Page 2 text"]})

    @patch("builtins.open", new_callable=mock_open)
    @patch("PyPDF2.PdfReader")
    def test_pdf_to_json_file_not_found(self, mock_pdf_reader, mock_open):
        # Simulate file not found error
        mock_open.side_effect = FileNotFoundError

        # Define file paths
        current_dir = os.path.dirname(__file__)
        pdf_file_path = os.path.join(current_dir, "nonexistent.pdf")
        json_file_path = os.path.join(current_dir, "output.json")

        # Capture the printed output
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            pdf_to_json(pdf_file_path, json_file_path)
            self.assertIn("An error occurred: ", fake_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()