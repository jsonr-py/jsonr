'''
setup jsonr > setup.py
'''

from setuptools import setup, find_packages
import pathlib

path_absolute: pathlib.Path = pathlib.Path(__file__).parent.absolute()

setup(
    name='jsonr',
    version='8.6.0',
    description='Highly customizable JSON objects and dataframes, and your python toolkit all in one.',
    long_description=pathlib.Path(f"{path_absolute}/README.md").read_text(encoding="utf-8"),
    long_description_content_type='text/markdown',
    url='https://github.com/jsonr-py/jsonr',
    author='jsonr',
    author_email='jsonr.py@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='jsonr json jsonr-py jsonr-python, python',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'numpy',
        'requests',
        'pathlib',
        'pandas',
        'google-generativeai'
    ]
)
