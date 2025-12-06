import requests
API_KEY = '0f10af919a46d191aa6c888e0cad5550'
celsius_symbol = "\u2103"
while True:
    city_name = input("Please enter your city name or press 'q' to quit: ")
    if city_name.lower() == "q":
        print("Goodbye")
        break
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print('Weather is',data['weather'][0]['description'])
        print('Temperature is',data['main']['temp'],f'{celsius_symbol}')
        print('Humidity is',data['main']['humidity'],'%')
    else:
            print("Sorry, we couldn't find the city")
