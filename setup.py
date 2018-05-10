from setuptools import setup, find_packages

packages = ['pytrie']

setup(
    name='pytrie',
    version='1.0.0',
    description='A packaged version of pytrie with extended length keys enabled.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Data Structures',
        'Programming Language :: Python :: 3.6'
    ],
    packages=packages
)
