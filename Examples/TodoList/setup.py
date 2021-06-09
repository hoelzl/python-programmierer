from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='todos',
    version='0.1',
    packages=find_packages(),
    entry_points={'console_scripts': [
        'todos = todos.__main__:main'
    ]},
    author='Matthias Hölzl',
    author_email='tc@xantira.com',
    description='A simple todo manager',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/mhoelzl/python-programmierer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
    ],
    python_requires='>=3.7',
)
