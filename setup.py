import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="datatable-faker",
    author="Prince Roshan",
    version='0.1.0',
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/Agent-Hellboy/datatable-faker",
    description=("Library to generate fake datatable for unittest "),
    long_description=read("README.rst"),
    license="MIT",
    package_dir={'': 'src'},
    packages=['datatable_faker'],
    keywords=[
        "faker","datatable-faker"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12-dev",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)