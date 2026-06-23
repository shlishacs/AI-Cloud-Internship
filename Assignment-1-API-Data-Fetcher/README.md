# API Data Fetcher

## Objective
This project demonstrates how to fetch data from two different APIs using Python.

## APIs Used

### 1. JSONPlaceholder API
- URL: https://jsonplaceholder.typicode.com/posts
- Purpose: Fetches sample post data for testing.
- Data Retrieved:
  - Post ID
  - Title
  - Body

### 2. OpenWeather API
- URL: https://api.openweathermap.org/data/2.5/weather
- Purpose: Fetches current weather information.
- Data Retrieved:
  - Temperature
  - Feels Like Temperature
  - Humidity
  - Weather Description
  - Wind Speed

## Requirements

Install the required library:

pip install requests

## How to Run

1. Open the project in PyCharm.
2. Install the requests library.
3. Add your OpenWeather API key in the code.
4. Run `api_fetcher.py`.

## Output

The program displays:
- First 5 posts from JSONPlaceholder API.
- Current weather information for Bangalore.
