from setuptools import find_packages, setup
from typing import List


HYPHEN_DOT_E  ='-e .'

def get_requirements(file_path:str)->List[str]:
    """
    Docstring for get_requirements
    This function will return the requirements 
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: List[str]
    """
    requirements =[]
    with open (file_path) as file_object:
        requirements = file_object.readlines()    # out put is ['pandas\n', 'numpy\n', 'seaborn\n'] -- has \n at end
        [req.replace('\n','') for req in requirements]

    if HYPHEN_DOT_E in requirements:
        requirements.remove(HYPHEN_DOT_E)
    
    return requirements
    

setup (
    name ='My Ml Project',
    version= '0.0.1',
    author='Yaswanth',
    author_email='katikalayaswanth@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)