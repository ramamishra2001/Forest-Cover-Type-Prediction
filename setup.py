from setuptools import setup ,find_packages

def get_requirements(path:str):
    with open(path,"r") as f:
        requirements=f.read().splitlines()
    requirements.pop(-1)
    return requirements


#hyperparameters
setup(
    name ='Forest_Cover_Type_Prediction',
    version ="0.0.1",
    description='Forest_Cover_Type_Prediction',
    author='Rama Mishra',
    author_email='rama.15mishra@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
