import json
import platform

from setuptools import setup, find_packages
import os

VERSION = '0.0.5'
NAME = "gitpyman"

with open("README.md","r",encoding="utf-8") as fp:
    long_description = fp.read()

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
      install_requires=[
          'docopt',
          'pyqt5',
          'lxml==4.2.1',
          'sqlalchemy',
          'github3.py',
          'eventlet'
      ],
      # copy .py file to python's Srcipts
      scripts=[],
      entry_points={
          'console_scripts': [
              'gitpyman = gitpyman.gm_run:run'# 这个是启动的exe命令
          ]
      },

      )

# import distutils.sysconfig

# PY_SITE_PACKAGES = distutils.sysconfig.get_python_lib(True)
# CONFIG_FILE_NAME = "~\\pip\\{}.json".format(NAME) if ("Windows" in platform.system()) else "~/.pip/{}.json".format(NAME)
# CONFIG_FILE_PATH = os.path.expanduser(CONFIG_FILE_NAME)
# CONFIG_DIR_PATH = os.path.dirname(CONFIG_FILE_PATH)
# if not os.path.exists(CONFIG_DIR_PATH):
    # os.mkdir(CONFIG_DIR_PATH)
## tpl-1.0.0-py3.6.egg
# PY = platform.python_version()  # 3.6.4
# EGG_NAME = NAME + "-" + VERSION + "-" + "py%s" % (str(PY)[:3]) + ".egg"
# EGG_DIR_PATH = os.path.join(PY_SITE_PACKAGES, EGG_NAME, )
# EGG_PATH = os.path.join(EGG_DIR_PATH, "source")

# with open(CONFIG_FILE_PATH, "w", encoding='utf8') as f:
    # f.write(json.dumps(
        # {"source_path": EGG_PATH},
        # ensure_ascii=False,
        # indent=4))
