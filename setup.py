import os

from setuptools import setup, find_packages

CLASSIFIERS = []

setup(
    name='django-simple-category',
    version='0.0.1',
    description='A simple to use categories app based on treebeard app.',
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README.rst')).read(),
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.6',
        'django-treebeard>=3.0',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
