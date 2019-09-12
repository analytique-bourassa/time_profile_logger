import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "time_profile_logger",
    version = "0.0.1",
    author = "Analytique Bourassa",
    author_email = "louis@analytiquebourassa.com",
    #description = ("An demonstration of how to create, document, and publish "
    #                               "to the cheese shop a5 pypi.org."),
   # license = "BSD",
   # keywords = "example documentation tutorial",
    #url = "http://packages.python.org/an_example_pypi_project",
    packages=['time_profile_logger'],
    long_description=read('README.md'),
   # classifiers=[
   #     "Development Status :: 3 - Alpha",
    #    "Topic :: Utilities",
   #     "License :: OSI Approved :: BSD License",
   # ],
)