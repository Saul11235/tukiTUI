#  script for local install

from os import system

system("pip uninstall tukiTUI")
system("python setup.py sdist bdist_wheel")
system("pip install .")
