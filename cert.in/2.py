from bs4 import BeautifulSoup


with open("nist.html", "r") as f:
    html_doc = f.read()


soup = BeautifulSoup(html_doc, 'html.parser')


s = soup.find('div', id="latestVulnsArea")


with open("x.html", "w") as output_file:
    if s:

        for child in s.children:
            output_file.write(str(child) + "\n")  
        print("Output successfully saved to x.html.")
    else:
        print("Div with id 'latestVulnsArea' not found.")
        output_file.write("Div with id 'latestVulnsArea' not found.")

