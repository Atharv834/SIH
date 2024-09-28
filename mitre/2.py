import requests
from bs4 import BeautifulSoup


with open("mitre.html", "r") as f:
    html_doc = f.read()


soup = BeautifulSoup(html_doc, 'html.parser')


div_with_id = soup.find(id="TableWithRules")


with open("x.html", "w") as output_file:
    if div_with_id:
        for child in div_with_id.children:
            output_file.write(str(child) + "\n")
        print("Output successfully saved to x.html.")
    else:
        print("Element with id 'TableWithRules' not found.")
        output_file.write("Element with id 'TableWithRules' not found.")

