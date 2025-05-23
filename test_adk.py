from google.adk import Agent
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your Gemini API key
api_key = os.getenv('GEMINI_API_KEY')

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }

def main():
    # Create an agent instance with weather capabilities
    agent = Agent(
        name="weather_agent",
        model="gemini-2.0-flash",
        description="Agent to answer questions about the weather in a city.",
        instruction="You are a helpful agent who can answer user questions about the weather in a city.",
        tools=[get_weather]
    )
    
    print("Weather agent is ready! Try asking about the weather in different cities.")
    # Get user input
    user_input = input("Enter your question: ")
    
    # Process user input using chat method
    response = agent.chat(user_input)
    
    # Print the response
    print(response)

if __name__ == "__main__":
    main() 