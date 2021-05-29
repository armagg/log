from setuptools import find_packages, setup

setup(
    name='mslog',
    packages=find_packages(),
    version='0.1.1',
    description='My log Python library',
    author='Mohammad saleh saeidi',
    license='MIT',
    install_requires=['kafka-python==2.0.2'],
    url="https://github.com/salehos/log",

)
