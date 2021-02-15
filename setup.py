from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy
import sys, os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if sys.platform.startswith('freebsd'):
  print("Detected Free BSD.")
  extra_objects = ["src/libs/fcio_linux.a", "src/libs/tmio-0.93_linux.a"]
elif sys.platform.startswith('linux'):
  print("Detected Linux")
  extra_objects = ["src/libs/fcio_linux.a", "src/libs/tmio-0.93_linux.a"]
elif sys.platform.startswith('darwin'):
  print("Detected Mac OS")
  extra_objects = ["src/libs/fcio_mac.a", "src/libs/tmio-0.93_mac.a"]
elif sys.platform.startswith('win32'):
  print("Detected Windows. Not supported!")
  sys.exit(1)

ext_modules = [Extension("fcutils",
                         sources = ["src/fcutils.pyx"],
                         include_dirs=["src/libs", numpy.get_include()],
                         #language='c++',
                         extra_objects=extra_objects
              )]

setup(
   name = "fcutils",
   version = "1.0.0",
   url = "https://git.mpi-hd.mpg.de/ssailer/pyfcutils",
   long_description=read('README.md'),
   ext_modules = cythonize(ext_modules, language_level=3),
   install_requires=[
      'cython'
   ]

)
