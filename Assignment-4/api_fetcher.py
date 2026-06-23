import requests

# -----------------------------------
# JSONPlaceholder API
# -----------------------------------

print("Fetching Posts from JSONPlaceholder...\n")

json_url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(json_url)

if response.status_code == 200:
    posts = response.json()

    print("First 5 Posts:\n")

    for post in posts[:5]:
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 40)
else:
    print("Failed to fetch posts.")

# -----------------------------------
# OpenWeather API
# -----------------------------------

print("\nFetching Weather Data...\n")

city = "Bangalore"

API_KEY = "2e771a9f430f6dbc9a100d4f62d319ff"

weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(weather_url)

if response.status_code == 200:
    weather = response.json()

    print("Current Weather in", city)
    print("Temperature:", weather["main"]["temp"], "°C")
    print("Feels Like:", weather["main"]["feels_like"], "°C")
    print("Humidity:", weather["main"]["humidity"], "%")
    print("Weather:", weather["weather"][0]["description"])
    print("Wind Speed:", weather["wind"]["speed"], "m/s")

else:
    print("Failed to fetch weather data.")
    print("Status Code:", response.status_code)s