import requests
import openpyxl

def main() -> None:

    countries = requests.get("https://restcountries.com/v3.1/all")
    countries = countries.json()

    planilha = openpyxl.Workbook()
    planilha.create_chartsheet('Countries')
    page_countries = planilha['Countries']

    page_countries.append(['Name', 'Capital', 'Area', 'Currencies'])
    page_countries.append([])


if __name__ == "__main__":
    main()