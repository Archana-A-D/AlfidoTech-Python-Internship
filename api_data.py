import requests  # Import requests module for API calls

try:
    # API URL
    url = "https://jsonplaceholder.typicode.com/users"

    # Send GET request to API
    response = requests.get(url)

    # Convert JSON response to Python data
    data = response.json()

    # Display user details
    for user in data:
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("--------------------")

except requests.exceptions.RequestException as e:
    # Handle API-related errors
    print("API Error:", e)