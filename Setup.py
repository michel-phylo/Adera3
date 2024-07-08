from setuptools import setup, find_packages
import subprocess
import sys
from pathlib import Path

# Function to install a package via pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])



# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='cancer type based on certain gene mutations',
    version='0.1',
    author='michel-phylo',
    author_email='@gmail.com',
    description='description of your project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/michel-phylo',  # Replace with your project's URL
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)

# Ensure 'shap' is installed
install_package('shap')
