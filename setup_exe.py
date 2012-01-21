from distutils.core import setup
from glob import glob
import py2exe, sys, os, shutil

sys.path.append("VSFILES")
data = [("Microsoft.VC90.CRT", glob(r'VSFILES\*.*'))]

setup(console=['start.py'],
      data_files=data,
      options={"py2exe":{"includes":["sip"]}},
      name="UXO",
      version="0.1",
      description="UXO app")

if os.path.isdir('dist/res/'):
    os.rmdir('dist/res/')

shutil.copytree('res/', 'dist/res/')


