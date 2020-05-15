# Message Queue

An example program that simulates a very simple message queue to
demonstrate Python packages and the distribution of Python programs.

Build source and binary distributions with the command

```shell script
python setup.py sdist bdist_wheel
```
in the root directory (i.e., the directory where `setup.py` lives.

To install the package, change into the `dist` directory and install it
with pip:

```shell script
cd dist
pip install .\msg_queue_mhoelzl-0.0.1.tar.gz
cd ..
```
