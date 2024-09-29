import requests
import os 
def fetchAndSaveToFile(url, path):
    try:
        r = requests.get(url)
        r.raise_for_status() 

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w", encoding='utf-8') as f:  
            f.write(r.text)
        print(f"Content successfully saved to {path}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except IOError as e:
        print(f"Error writing to file: {e}")

keyword = input("Enter the Device name: ")

url = f"https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={keyword}"

fetchAndSaveToFile(url, r"C:\Users\Atharv\Desktop\Chatgpt\SIH\mitre\mitre.html")
