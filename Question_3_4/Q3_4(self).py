import os
import zipfile

txt_files = []
for file_name in os.listdir('.'):
    if file_name.endswith('.txt') and os.path.isfile(file_name):
        txt_files.append(file_name)

count = len(txt_files)

if count > 0:
    with zipfile.ZipFile("mytxt.zip", "w") as zipf:
        for file in txt_files:
            zipf.write(file)
    print(f"There are {count} .txt files and they have been compressed into 'mytxt.zip'")
else:
    print("There are 0 .txt files. No compression performed.")
