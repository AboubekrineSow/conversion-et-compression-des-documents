import zipfile

def compress_file(file_path):
    if file_path:
        zip_path = file_path + '.zip'
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(file_path, arcname=file_path.split("/")[-1])
        return zip_path
    else:
        return None

def decompress_file(zip_file):
    if zip_file.endswith('.zip'):
        try:
            extraction_path = zip_file.replace('.zip', '')
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(extraction_path)
            return extraction_path
        except Exception as e:
            print(f"Erreur lors de la décompression : {e}")
            return None
    else:
        return None
