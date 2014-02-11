#!/usr/bin/env python

from setuptools import setup


setup(name='projectname',
      version='0.0.1',
      description='',
      long_description=open('README.md', 'rt').read(),
      license='',
      author='',
      url='https://github.com/tobigue',

      install_requires=[
      ],

      entry_points={
          'console_scripts': [
              'hello = projectname.__init__:test',
          ]
      }
      )
