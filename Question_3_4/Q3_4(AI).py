import glob
import zipfile

txt_files = glob.glob("*.txt")
file_count = len(txt_files)

if file_count > 0:
    with zipfile.ZipFile("mytxt.zip", "w") as zipf:
        for file in txt_files:
            zipf.write(file)
    print(f"{file_count} .txt files were compressed into 'mytxt.zip'.")
else:
    print("No .txt files detected. Compression skipped.")
