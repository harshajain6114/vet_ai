import requests

def run():
    """
    Calls the API to run the crew.
    """
    url = "http://127.0.0.1:5000/run"
    
    try:
        response = requests.post(url, timeout=10)  # Added timeout for better reliability
        
        if response.status_code == 200:
            print("✅ Crew started successfully!")
            print(response.json())  
        else:
            print(f"❌ Error starting crew: {response.status_code} - {response.text}")
    
    except requests.exceptions.ConnectionError:
        print("❌ Failed to connect to the API. Ensure the server is running.")
    except requests.exceptions.Timeout:
        print("⏳ Request timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    run()
