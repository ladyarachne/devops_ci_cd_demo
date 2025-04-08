import requests

def main():
    url = "http://example.com"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"✅ Success: Able to reach {url}")
    else:
        print(f"❌ Error: Status {response.status_code}")

if __name__ == "__main__":
    main()
