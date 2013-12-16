try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

#classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers
setup(
    name = "project",
    version = "0.0.4",
    author = "Your Name",
    author_email = "youremail@email.com",
    description = ("A short description of "
                                   "your project"),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://yourproject.com",
    packages = ['project', 'test'],
    long_description = read('README.md'),
    classifiers =
        [
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: BSD License",
        ],
    )
