from setuptools import find_packages,setup
from typing import List
import pkg_resources


HYPEN_E_DOT='-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    this function will return list of requirement
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    missing_packages = [req for req in requirement if req.lower() not in installed_packages]

    if missing_packages:
        print("Missing packages:", missing_packages)
    else:
        print("All packages are installed.")

    return requirement


setup(name='ml-project',
      version='0.0.1',
      author='Anant',
      author_email='anantlad0628@gmail.com',
      packages=find_packages(),
      install_requires=get_requirement('requirement.txt')
      )