import zipfile

def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    archive_path = "C:/Users/Elliot.Smith/Desktop/Documents/Promotions/Scripts/Tutorials/Python/python_mega_course_60day/File_Extractor/test archive.zip"
    dest_dir = "C:/Users/Elliot.Smith/Desktop/Documents/Promotions/Scripts/Tutorials/Python/python_mega_course_60day/File_Extractor"
    extract_archive(archive_path, dest_dir)