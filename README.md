# pdfToJson

## Project Description

The `pdfToJson` project is a Python script that converts the text content of a PDF file into a JSON format. This can be useful for extracting and processing text data from PDF documents for various applications.

## Installation Instructions

### Setting Up a Virtual Environment

To create a virtual environment for this project, follow these steps:

1. Ensure you have Python installed on your system. You can download it from the official Python website if needed.
2. Open a terminal or command prompt.
3. Navigate to the root directory of the project where the `pdfToJson.py` file is located.
4. Run the following command to create a virtual environment named `venv`:
   ```
   python -m venv venv
   ```
5. Activate the virtual environment:
   - On Windows, run:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux, run:
     ```
     source venv/bin/activate
     ```

### Installing Dependencies

To install dependencies using `requirements.txt`, follow these steps:

1. Ensure you have activated the virtual environment. If not, activate it using the appropriate command for your operating system.
2. Create a `requirements.txt` file in the root directory of the project if it doesn't already exist. This file should list all the required dependencies, one per line. For example:
   ```
   PyPDF2
   pytest
   ```
3. Run the following command to install the dependencies listed in the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

## Usage Instructions

To run the `pdfToJson.py` script, follow these steps:

1. Ensure you have set up the virtual environment and installed the required dependencies as described in the installation instructions.
2. Open a terminal or command prompt.
3. Navigate to the root directory of the project where the `pdfToJson.py` file is located.
4. Run the following command to execute the script:
   ```
   python pdfToJson.py
   ```

## Running Tests

To run tests using `pytest`, follow these steps:

1. Ensure you have set up the virtual environment and installed the required dependencies as described in the installation instructions.
2. Open a terminal or command prompt.
3. Navigate to the root directory of the project.
4. Run the following command to execute the tests:
   ```
   pytest
   ```

## Contributing Guidelines

We welcome contributions to the `pdfToJson` project. To contribute, follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name for your feature or bug fix.
3. Make your changes and commit them with clear and concise commit messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository, describing your changes and the purpose of the contribution.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
