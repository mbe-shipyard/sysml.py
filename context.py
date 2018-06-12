"""
context.py
~~~~~~~~~~
Access main module from tests folder
"""

import os
import sys

basepath = os.path.abspath(os.path.join(os.path.dirname(__file__),'../sysml'))
sys.path.insert(0, basepath)
import sysml

print('inserting path ', basepath)
