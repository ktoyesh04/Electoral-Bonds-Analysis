import PyPDF2
import re
import csv

def read_pdf(pdf_file):
    """
    Function to read text content from a PDF file.
    
    Args:
        pdf_file (str): Path to the PDF file.
    
    Returns:
        str: Text content extracted from the PDF.
    """
    with open(pdf_file, 'rb') as file:
        text = ""
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for pageNum in range(num_pages):
            page = reader.pages[pageNum]
            text += page.extract_text()
    return text

def to_csv(pattern, text, csv_file, header):
    """
    Function to extract data based on a pattern and write it to a CSV file.
    
    Args:
        pattern (str): Regular expression pattern to extract data from text.
        text (str): Text content containing the data.
        csv_file (str): Path to the CSV file to write the data.
        header (list): List containing column headers for the CSV file.
    """
    # Extract data into a list of tuples
    data = re.findall(pattern, text)

    # Write data to CSV
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data)

    print("Conversion completed successfully!")

# Configuration for political party data
party_pdf_file = "EB_Encashment_Detailed.pdf"
party_csv_file = "EB_Party.csv"
party_file_header = ['Sr No', 'Date of Encashment', 'Name of the Political Party', 'Account no. of Political Party',
                     'Prefix', 'Bond Number', 'Denominations', 'Pay Branch Code', 'Pay Teller']
party_row_pattern = r'(\d+) (\d+/\w+/\d+) (.+?) (\*{7}\d+) (\w+) (\d+) ([\d,]+) (\d+) (\d+)'

# Read PDF and convert to CSV for political party data
text = read_pdf(party_pdf_file)
to_csv(party_row_pattern, text, party_csv_file, party_file_header)

# Configuration for purchasers data
purchaser_pdf_file = "EB_Purchasers_Detailed.pdf"
purchaser_csv_file = "EB_Purchasers.csv"
purchaser_file_header = ['Sr No', 'Reference No (URN)', 'Journal Date', 'Date of Purchase', 'Date of Expiry',
                         'Name of the Purchaser', 'Prefix', 'Bond Number', 'Denominations', 'Issue Branch Code',
                         'Issue Teller', 'Status']
purchaser_row_pattern = r'(\d+) (\S+) (\d+/\w+/\d+) (\d+/\w+/\d+) (.+?) (.+?) ([A-Z]+) (\d+) ([\d,]+) (\S+) (\d+) (\w+)'

# Read PDF and convert to CSV for purchasers data
text = read_pdf(purchaser_pdf_file)
to_csv(purchaser_row_pattern, text, purchaser_csv_file, purchaser_file_header)
