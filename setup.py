from setuptools import find_packages, setup
from typing import List

hyphon_e_dot = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ req.replace('\n','') for req in requirements]

        if hyphon_e_dot in requirements:
            requirements.remove(hyphon_e_dot)
    return requirements    


setup(
    name="ML Project",
    version="0.0.1",
    author="Saugat Bhattarai",
    author_email="saugatme@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)