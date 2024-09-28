import requests
from bs4 import BeautifulSoup


with open("ndvt.html", "r") as f:
    html_doc = f.read()


soup = BeautifulSoup(html_doc, 'html.parser')


s = soup.find(class_="searchby unstriped scroll")


with open("x.html", "w") as output_file:
    if s:

        for child in s.children:
            output_file.write(str(child) + "\n")
        print("Output successfully saved to x.html.")
    else:
        print("Element with class 'searchby unstriped scroll' not found.")
        output_file.write("Element with class 'searchby unstriped scroll' not found.")

