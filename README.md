# Create a new virtual environment
python3 -m venv ./venv

# Install and create virtual environment
pip install virtualenv
virtualenv venv

# activate virtual environment
venv\Scripts\activate

# Deactivate virtual environment 
deactivate

# Install dependencies
pip install pysimplegui==4.60.5
pip install pyinstaller

# Install specific version of dependancies
pip install package_name==desired_version

# Check dependancy is installed
pip show package_name

# Uninstall dependancy
pip uninstall library_name

# Create executable
pyinstaller --onefile --windowed --clean main.py

# pip3 install -r requirements.txt