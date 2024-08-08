import urllib.parse
import urllib.request
import json

user_string = input("String to convert into leetspeak: ")

# Encode the user input to be used in the URL
encoded_user_string = urllib.parse.quote_plus(user_string)

# Construct the URL with encoded user input
url_ultra = f"https://genr8rs.com/api/Content/Fun/LeetSpeakGenerator?_sText={encoded_user_string}%0A&_sCharacterSet=ultra"

# Send a GET request to the URL
with urllib.request.urlopen(url_ultra) as response:
    # Read the response
    response_data = response.read().decode("utf-8")
    # Parse the JSON response
    response_json = json.loads(response_data)
    # Extract the leetspeak result
    leetspeak_result = response_json["_sResult"]
    print(
        "Ultra Leetspeak version:", leetspeak_result.strip()
    )  # Remove trailing newline character
