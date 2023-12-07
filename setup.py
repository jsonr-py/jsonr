from setuptools import setup, find_packages

setup(
    name='jsonr',
    version='8.5.1',
    description='Highly customizable JSON objects and dataframes.',
    long_description='README.md',
    long_description_content_type='text/markdown',
    url='https://github.com/jsonr-py/jsonr',
    author='jsonr',
    author_email='jsonr.py@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='jsonr json jsonr-py jsonr-python, dataframe, df, pandas, python',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'numpy'
    ]
)
