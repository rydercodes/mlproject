from setuptools import setup, find_packages
from typing import List

HYPHER_E_DOT='-e .'
def get_requirements(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        lines = f.readlines()
        if HYPHER_E_DOT in lines:
            lines.remove(HYPHER_E_DOT)
    return [line.strip() for line in lines]
requirements = get_requirements('requirements.txt')


setup(
    name='mlproject',
    version='0.1',
    author='Jaber',
    author_email='Jaber.rahimifard@outlook.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)