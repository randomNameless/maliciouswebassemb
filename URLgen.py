import os

# Folder containing the HTML files
html_folder = '/home/selab/Desktop/maliciouswebassemb'  # Replace with the actual path to your HTML folder

# Base URL prefix
base_url = 'https://randomnameless.github.io/maliciouswebassemb/'

# Output file path (where the URLs will be saved)
output_file = 'urls_list.txt'

# Get a list of all HTML files in the folder
html_files = [f for f in os.listdir(html_folder) if f.endswith('.html')]

# Open the output file for writing
with open(output_file, 'w') as file:
    # Iterate through the HTML files and create the corresponding URLs
    for html_file in html_files:
        # Generate the URL
        url = base_url + html_file
        # Write the URL to the file, one URL per line
        file.write(url + '\n')

print(f"URL list has been generated and saved to {output_file}.")

