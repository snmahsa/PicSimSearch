from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='PicSimSearch',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    description=' Python package for image search based on keypoint-based feature extraction and matching ',
    author='Mahsa Sanaei',
    author_email='mahsasanaei.n@gmail.com',
    packages=['PicSimSearch']
    )