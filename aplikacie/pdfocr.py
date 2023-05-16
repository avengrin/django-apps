# nainstalovat pip install ocrmypdf ak nie je
# spustit python aplikacie/pdfocr.py

import ocrmypdf

def main():
    zdroj = input('Nazov pdf suboru: ')
    ciel = input('Nazov noveho suboru: ')
    ocrmypdf.ocr(zdroj, ciel, deskew=True, language='slk')

if __name__ == '__main__':
    main()