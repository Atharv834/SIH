from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate


filename = r'kbcert.org\x.html'
with open(filename, 'r') as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, 'html.parser')


headers = [th.get_text(strip=True) for th in soup.find_all('thead')[0].find_all('th')]


rows = []
base_url = "https://www.kb.cert.org" 

for tr in soup.find_all('tbody')[0].find_all('tr'):
    # Exclude the row containing "Updates"
    if 'Updates' not in tr.get_text():
        row = []
        for td in tr.find_all('td'):
            # Check if the <td> has an <a> tag inside
            link = td.find('a')
            if link:
                # If <a> tag exists, format as clickable link with the base URL
                full_url = f"{base_url}{link['href']}"
                row.append(f"<a href='{full_url}'>{link.text.strip()}</a>")
            else:
                # Otherwise, just add the text content
                row.append(td.get_text(strip=True))
        rows.append(row)

# Create a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Convert DataFrame to HTML with proper table formatting
html_output = df.to_html(index=False, border=1, escape=False, classes='table table-striped')

# Save HTML output to a file
with open('kbcert.org/output.html', 'w') as file:
    file.write(html_output)

# Convert DataFrame to string format using tabulate for proper alignment
text_output_str = tabulate(df, headers='keys', tablefmt='grid', showindex=False)

# Save text output to a .txt file
with open('output.txt', 'w') as file:
    file.write(text_output_str)

print("HTML and text outputs have been saved to 'output.html' and 'output.txt', respectively.")

