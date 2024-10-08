import requests

def fetchAndSaveToFile(url, path):
    try:

        r = requests.get(url)
        r.raise_for_status()  


        with open(path, "w") as f:
            f.write(r.text)
        print(f"Content successfully saved to {path}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except IOError as e:
        print(f"Error writing to file: {e}")

url = "https://www.kb.cert.org/vuls/bypublished/desc/"
fetchAndSaveToFile(url, r"C:\Users\Atharv\Desktop\Chatgpt\SIH\kbcert.org\ndvt.html")

