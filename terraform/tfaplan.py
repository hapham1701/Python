import os
import re
import sys
import subprocess
import pyperclip

# get the filename from command line argument
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = None
    
if len(sys.argv) > 2:
    target_resource = sys.argv[2]
else:
    target_resource = None


def aplan():
    print('atlantis plan --',end =" ")
    with open(filepath, 'r') as file:
        count_resource = 0
        count_module = 0
        
        for line in file:
            if target_resource =='resource' and 'resource "' in line:
                count_resource += 1
                line = line.rstrip()
                match = re.search(r'("[^ ]+") ("[^ ]+")', line)
                if match:
                    resource_name = match.group(1)
                    context = match.group(2)
                    print(f'-target {resource_name}.{context}',end =" ")   
            elif target_resource =='module' and 'module "' in line:
                count_module += 1
                line = line.rstrip()
                match = re.search(r'("[^ ]+")', line)
                if match:
                    resource_name = match.group(1)
                    print(f'-target module.{resource_name}',end =" ")
            elif target_resource == None:
                if 'resource "' in line:
                    count_resource += 1
                    line = line.rstrip()
                    match = re.search(r'("[^ ]+") ("[^ ]+")', line)
                    if match:
                        resource_name = match.group(1)
                        context = match.group(2)
                        print(f'-target {resource_name}.{context}',end =" ")
                if 'module "'  in line:
                    count_module += 1
                    line = line.rstrip()
                    match = re.search(r'("[^ ]+")', line)
                    if match:
                        resource_name = match.group(1)
                        print(f'-target module.{resource_name}',end =" ")
                    
    print(f'\n\nNumber of Resoure target is: {count_resource}')
    print(f'Number of Module target is: {count_module}')   


if filename == None:
    clipboard_content = pyperclip.paste()     # Save the clipboard content to a file
    with open('/Users/hapham/python/select.tf', 'w') as f:
        f.write(clipboard_content)
    filepath='/Users/hapham/python/select.tf'
    aplan()
    
else:
    filepath = os.path.join(os.getcwd(), filename)
    aplan()
print("\n\n-----------------------------")

