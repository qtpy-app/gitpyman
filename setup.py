import json
import platform

from setuptools import setup, find_packages
import os

VERSION = '0.0.6'
NAME = "gitpyman"

with open("README.md","r",encoding="utf-8") as fp:
    long_description = fp.read()

BASE_REQUIRES =[
          'docopt',
          'lxml==4.2.1',
          'sqlalchemy',
          'github3.py',
          'eventlet',
      ]
global REQUIRES
try:
    from PyQt5.QtCore import QT_VERSION_STR
    if tuple(map(int,QT_VERSION_STR.split("."))) > (5,10,1):
        REQUIRES = BASE_REQUIRES + [
                  'pyqt5',
                  'PyQtWebEngine',
              ]
    else:
        REQUIRES = BASE_REQUIRES
        
except:
    REQUIRES = BASE_REQUIRES + [
            'pyqt5==5.10.1',
    ]
      
setup(name=NAME,
      version=VERSION,
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python、PyQt5、github Manage',
      author='Lin JH',
      author_email='625781186@qq.com',
      url='https://github.com/625781186/gitpyman',
      license='GPL-3.0',
      description="comment your github.",
      long_description=long_description,
      long_description_content_type='text/markdown',  # This is important
      # --------------------------------------------#
      # package_dir={'source': './gitpyman'},
      packages=find_packages(),
      include_package_data=True,  # 和下面的写法冲突

      # package_data={
      #     "": ["*"],
      # },

      zip_safe=False,
      python_requires='>=3.6',
      install_requires=REQUIRES,
      # copy .py file to python's Srcipts
      scripts=[],
      entry_points={
          'console_scripts': [
              'gitpyman = gitpyman.gm_run:run'# 这个是启动的exe命令
          ]
      },

      )


