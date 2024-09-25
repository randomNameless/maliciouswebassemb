import os
import re
import subprocess
from bs4 import BeautifulSoup

# Folder paths
html_folder = '/home/selab/Desktop/HTMLTransfer'  # Set your path to the folder containing HTML files
input_js_path = 'input.js'
output_js_path = 'output.js'
config_path = '/home/selab/Desktop/wobfuscator_tool/Wobfuscator/build/config.json'  # Path to the config file for the tool
node_tool_path = '/home/selab/Desktop/wobfuscator_tool/Wobfuscator/build/index.js'  # Path to your Node tool

# Iterate over all HTML files in the folder
for filename in os.listdir(html_folder):
    if filename.endswith('.html'):
        html_file_path = os.path.join(html_folder, filename)

        # Read the HTML file
        with open(html_file_path, 'r', encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')

            # Find the <script> tag with JavaScript code
            script_tag = soup.find('script')
            if script_tag and script_tag.string:
                js_code = script_tag.string.strip()

                # Write the JavaScript code to input.js
                with open(input_js_path, 'w', encoding='utf-8') as input_js_file:
                    input_js_file.write(js_code)

                # Run the tool to generate output.js
                subprocess.run(['node', node_tool_path, '-f', input_js_path, '-o', output_js_path, '-c', config_path])

                # Read the generated output.js code
                with open(output_js_path, 'r', encoding='utf-8') as output_js_file:
                    output_js_code = output_js_file.read().strip()

                # Replace the JavaScript in the <script> tag with the new code from output.js
                script_tag.string.replace_with(output_js_code)

                # Save the modified HTML back to the file
                with open(html_file_path, 'w', encoding='utf-8') as modified_html_file:
                    modified_html_file.write(str(soup))

print("All HTML files have been processed.")

