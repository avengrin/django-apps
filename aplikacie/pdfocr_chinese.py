# nainstalovat pip install ocrmypdf ak nie je
# spustit python aplikacie/pdfocr.py

import ocrmypdf

def main():
    zdroj = input('Nazov pdf suboru: ')
    ciel = input('Nazov noveho suboru: ')
    # SK: ocrmypdf.ocr(zdroj, ciel, deskew=True, language='slk')
    ocrmypdf.ocr(zdroj, ciel, deskew=True, language='chi_sim')
    

if __name__ == '__main__':
    main()
