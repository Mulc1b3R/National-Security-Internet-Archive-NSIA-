from bs4 import BeautifulSoup

# Read the contents of your HTML file
with open('links.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <a> tags and update the href attribute and wrap with <li> tags
for link in soup.find_all('a', href=True):
    # Update the href attribute with the appended URL
    link['href'] = 'https://archive.org/download/' + link['href']
    # Wrap the <a> tag with <li> tags
    link.wrap(soup.new_tag("li"))

# Save the updated HTML content to a new file
updated_html = str(soup)
with open('updated_html_file.html', 'w') as file:
    file.write(updated_html)