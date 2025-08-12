import requests
import json

URL = "https://api.nbp.pl/api/exchangerates/tables/a"

data = requests.get(URL)
json_data = json.loads(data.content)

waluta_uzytkownika = input(str("Podaj jaką walutę chcesz sprawdzić: "))

znaleziona = False
try:
    for i in range(len(json_data[0]['rates'])):
        for j in json_data[0]['rates'][i]:
            if json_data[0]['rates'][i]['code'] == waluta_uzytkownika.upper():
                print(f"{j}: {json_data[0]['rates'][i][j]}")
                znaleziona = True
    if not znaleziona:
        raise NameError("Podana waluta nie zawiera się w zbiorze!!!!")
except NameError as error:
    print(error)
    
        

# print(json_data[0]['rates'][0]['code'])
# print(json_data[0]['rates'][0]['mid'] )