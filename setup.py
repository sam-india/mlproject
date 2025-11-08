from setuptools import setup, find_packages

HYPHON_E_D = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''This function will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHON_E_D in requirements:
            requirements.remove(HYPHON_E_D)
        return requirements

setup(  name='mlproject',
    version='0.1.0',
    author='Sam',
    authoe_email='sajal.samaiya.06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'),
    description='A machine learning project setup',
)

