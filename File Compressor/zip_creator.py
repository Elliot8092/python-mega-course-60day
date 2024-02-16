import zipfile
import pathlib

def archive_files(filepaths, dest_dir, archive_name):
    with zipfile.ZipFile(dest_dir + "/" + archive_name + ".zip", 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
