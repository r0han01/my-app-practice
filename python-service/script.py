import requests

def fetch_node_message():
    url = "http://backend:3000/message"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Message from Node.js: {data['message']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_node_message()
