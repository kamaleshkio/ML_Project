from setuptools import setup, find_packages
from typing import List

HPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]: 
    '''Get the requirements from the file'''

    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HPEN_E_DOT in requirements:
            requirements.remove(HPEN_E_DOT)
    
    return requirements
    

setup(
    name='mlproject',
    version='0.0.1',
    author='kamalesh',
    author_email='kamaleshbaskaran4310@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))