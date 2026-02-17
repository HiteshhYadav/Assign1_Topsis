from setuptools import setup, find_packages
import os

# Function to read the README file for the long description
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8").read()

setup(
    name="Topsis-Hitesh-102317248", 
    version="1.0.1",
    author="Hitesh Yadav",
    author_email="yadavhitesh144@gmail.com",
    description="A command-line Python package to implement the TOPSIS method.",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/HiteshhYadav/Assign1_Topsis",
    
    # Since setup.py is in the same folder as the package folder, use find_packages()
    packages=find_packages(), 
    
    install_requires=[
        'pandas',
        'numpy', 
    ],
    
    entry_points={
        'console_scripts': [
            'topsis=topsis_hitesh_102317248.cli:main',
        ],
    },
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
    ],
    python_requires='>=3.6',
)