from setuptools import setup, find_packages

setup(
    name='mark-my-kindle-citations',
    version='0.1',
    description='A tool to convert Kindle citations to markdown.',
    author='Jaroslaw Mroz',
    author_email='jrs.mroz@gmail.com',
    py_modules=['run'],
    install_requires=[
        'beautifulsoup4>=4.9.0',
    ],
    entry_points={
        'console_scripts': [
            'mark-my-kindle-citations = run:main',
        ],
    },
)
