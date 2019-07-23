"""PYGITC
Usage:
  pygitc run
  pygitc (-h | --help)
  pygitc (-v | --version)
Options:
  run
  -h --help        Show this screen.
  -v --version     Show version.
"""
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
sys.path.append(os.path.dirname(__file__))
from docopt import docopt

try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView
except:
    print("If your pyqt version>5.10.1 , please pip install PyQtWebEngine")

from Client import main
APP_DESC = """
         PYGITC ---- PyQt5 template
         @author qq 625781186  (https://github.com/625781186/github_comment) 
"""

NAME = "github_comment"



def start():
    main()


def run():
    sys.argv.append("run")
    arguments = docopt(__doc__, version="0.0.1")
    print(arguments)
    if arguments["run"]:

        ok = start()

        if ok:
            print("Success!")
        else:
            print("Fail!")
    else:
        print("input error!")


if __name__ == "__main__":
    # print(APP_DESC)
    # print(sys.argv)
    # sys.argv.append("run")

    run()
