import zipfile

def unzip_file(zip_file, output_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

unzip_file('input.zip', '/DataCloudDSL')