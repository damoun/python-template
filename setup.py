#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changelog_file:
    changelog = changelog_file.read()

setup(
    author="Damien PLENARD",
    author_email='damien@plenard.me',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A Github template for Python project repository.",
    entry_points={
        'console_scripts': [
            'python-template=python_template.cli:main',
        ],
    },
    license="MIT License",
    long_description=readme + '\n\n' + changelog,
    include_package_data=True,
    keywords='icrawlerbot',
    name='icrawlerbot',
    packages=find_packages(include=['python_template']),
    test_suite='tests',
    url='https://github.com/damoun/python-template',
    version="0.0.1",
    zip_safe=False,
)
