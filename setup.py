#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='projectname',
      version='0.0.1',
      description='',
      long_description=open('README.md', 'rt').read(),
      license='',
      author='',
      url='https://github.com/tobigue',

      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,

      install_requires=[
      ],

      entry_points={
        'console_scripts': [
        'hello = projectname.__init__:test',
        ]
      }
     )
