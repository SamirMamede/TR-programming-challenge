import requests
import openpyxl

def main() -> None:

    url = "https://restcountries.com/v3.1/all"

    countries = requests.get(url)
    data = countries.json()

    planilha = openpyxl.Workbook()
    planilha.create_sheet('Country')
    page_countries = planilha['Country']

    page_countries.append(['Name', 'Capital', 'Area', 'Currencies'])


    for i in range (len(data)):
        
        countries_name = data[i]['name']['common']
        try:
            countries_capital = data[i]['capital']
            for key in countries_capital:
                countries_capital = key
        except:
            countries_capital = '-' 
        countries_area = data[i]['area']
        try:
            countries_currencies = data[i]['currencies']
            for key in countries_currencies:
                countries_currencies = key
        except:
            countries_currencies = '-'

        page_countries.append([countries_name, countries_capital, countries_area, countries_currencies])
    
    planilha.save('Countries list.xlsx')


if __name__ == "__main__":
    main()