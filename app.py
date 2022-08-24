import requests
import openpyxl

def main() -> None:

    url = "https://restcountries.com/v3.1/all"

    countries = requests.get(url)
    data = countries.json()

    for i in range (len(data)):
        countries_name = data[i]['name']['official']
        countries_capital = data[i]['capital'][0]
        countries_area = data[i]['area']
        countries_currencies = data[i]['currencies']
        for key in countries_currencies:
            countries_currencies = key

        print(countries_name)
        print(countries_capital)
        print(countries_area)
        print(countries_currencies)


#    planilha = openpyxl.Workbook()
#    planilha.create_chartsheet('Countries')
#    page_countries = planilha['Countries']

#    page_countries.append(['Name', 'Capital', 'Area', 'Currencies'])
#    page_countries.append([])


if __name__ == "__main__":
    main()