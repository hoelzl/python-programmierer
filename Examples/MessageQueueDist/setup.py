import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='msg_queue_mhoelzl',
    version='0.0.1',
    author='Matthias Hölzl',
    author_email='tc@xantira.com',
    description='Example project for packaging',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/mhoelzl/python-programmierer',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
    ],
    python_requires='>=3.7',
)
