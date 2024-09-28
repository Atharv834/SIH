from bs4 import BeautifulSoup

# Load the HTML content from the file
with open('x.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the list of vulnerabilities
vulns_list = soup.find(id='latestVulns')

# Define the base URL
base_url = 'https://nvd.nist.gov/'

# Extract vulnerability details
vulnerabilities = []
for li in vulns_list.find_all('li')[:20]:  # Get only the latest 20 items
    # Get CVE ID and URL
    cve_link = li.find('a')
    cve_id = cve_link.text
    cve_url = base_url + cve_link['href']  # Concatenate base URL with CVE URL
    
    # Get CVE summary
    summary = li.find('div', class_='col-lg-9').find('p').text.strip()
    
    # Get CVSS score and severity
    cvss_score = li.find('span', id=lambda x: x and x.startswith('cvss3-link-')).find('a').text
    severity = cvss_score.split()[1]  # Extract severity from the CVSS score

    vulnerabilities.append({
        'CVE ID': cve_id,
        'URL': cve_url,
        'Summary': summary,
        'CVSS Score': cvss_score,
        'Severity': severity
    })

# Generate HTML table
html_table = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vulnerability List</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 16px;
            text-align: left;
        }
        th, td {
            padding: 12px;
            border: 1px solid #ddd;
        }
        th {
            background-color: #f4f4f4;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
    </style>
</head>
<body>
    <h1>Latest Vulnerabilities</h1>
    <table>
        <thead>
            <tr>
                <th>CVE ID</th>
                <th>URL</th>
                <th>Summary</th>
                <th>CVSS Score</th>
                <th>Severity</th>
            </tr>
        </thead>
        <tbody>
"""

# Add rows to the table
for vuln in vulnerabilities:
    html_table += f"""
        <tr>
            <td>{vuln['CVE ID']}</td>
            <td><a href="{vuln['URL']}" target="_blank">{vuln['URL']}</a></td>
            <td>{vuln['Summary']}</td>
            <td>{vuln['CVSS Score']}</td>
            <td>{vuln['Severity']}</td>
        </tr>
    """

html_table += """
        </tbody>
    </table>
</body>
</html>
"""

# Save the HTML table to a file
with open('vulnerabilities.html', 'w', encoding='utf-8') as file:
    file.write(html_table)

print("HTML file 'vulnerabilities.html' created successfully.")

