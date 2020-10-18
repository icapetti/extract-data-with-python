# Install tabula and requests: pip install tabula-py and pip install requests
# Imports
import requests as req
import tabula as tb

# Function to download pdf file
def download_file(url, file_path):
    response = req.get(url)
    if response.status_code == req.codes.OK:
        with open(file_path, 'wb') as new_file:
                new_file.write(response.content)
        print("PDF Downloaded: {}".format(file_path))
    else:
        response.raise_for_status()


def main():
    # Link dos dados se auxilio de imoveis para os senadores:
    # http://www.senado.gov.br/transparencia/lai/secrh/senador_auxilio_imoveis_pdf.pdf

    pdf_file = "pdf_file.pdf"
    csv_file = "csv_file.csv"
    
    url = input('URL: ')
    path = input('PATH: ')

    download_file(url, path+pdf_file)

    try:
        tb.convert_into(path+pdf_file, path+csv_file, output_format="csv", pages="all")
        print("PDF converted and CSV saved.")
    except:
        print("Something went wrong.")

main()