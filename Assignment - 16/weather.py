import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> None:
    """
    Fetch and display current weather for the given city.

    Privacy Note:
    The city name (location data) is intentionally NOT logged to the console
    or any log file. Logging user location data — even seemingly harmless inputs
    like city names — can constitute a violation of user privacy under laws such
    as the GDPR (General Data Protection Regulation, EU) and HIPAA (Health
    Insurance Portability and Accountability Act, US). In a healthcare context,
    location data combined with other identifiers may be considered Protected
    Health Information (PHI). Logging it creates an audit trail of patient
    behaviour that must be avoided unless explicit consent is obtained and proper
    data-handling safeguards are in place.
    """

    if not API_KEY:
        print("Error: OPENWEATHER_API_KEY is not set. Please check your .env file.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        # Task 2 — Handle rate limiting gracefully
        if response.status_code == 429:
            print(
                "Weather service is temporarily unavailable due to too many requests. "
                "Please try again in a minute."
            )
            return

        if response.status_code == 401:
            print("Authentication failed. Please check your API key.")
            return

        if response.status_code == 404:
            print("City not found. Please check the city name and try again.")
            return

        if response.status_code != 200:
            print(f"Unexpected error from weather service (status {response.status_code}). Please try again later.")
            return

        data = response.json()
        description = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        print("\n--- Weather Alert ---")
        print(f"Condition : {description}")
        print(f"Temperature : {temp}°C (Feels like {feels_like}°C)")
        print(f"Humidity  : {humidity}%")
        print("---------------------\n")

    except requests.exceptions.ConnectionError:
        print("Network error: Unable to reach the weather service. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. The weather service took too long to respond.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected network error occurred: {e}")


if __name__ == "__main__":
    city_input = input("Enter city name: ").strip()
    if city_input:
        get_weather(city_input)
    else:
        print("No city entered. Please provide a valid city name.")
