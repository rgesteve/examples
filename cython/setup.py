import platform
from setuptools import setup, Extension
from Cython.Distutils import build_ext
import numpy as np

NAME = "simple-cython-example"
VERSION = "0.1"
DESCR = "A small template project that shows how to wrap C/C++ code into python using Cython"
URL = "http://www.google.com"
REQUIRES = ['numpy', 'cython']

AUTHOR = "Tristan A. Hearn"
EMAIL = "tristanhearn@gmail.com"

LICENSE = "Apache 2.0"

SRC_DIR = "cython_example_proj"
PACKAGES = [SRC_DIR]

IS_WINDOWS = (platform.system() == 'Windows')
IS_LINUX = (platform.system() == 'Linux')

if IS_WINDOWS:
    extra_link_args = ['/DEBUG:FULL']
    extra_compile_args = ['/Zi', '/Od']
else:
    extra_link_args = []
    extra_compile_args = ['-g']

ext_1 = Extension(SRC_DIR + ".wrapped",
                  [SRC_DIR + "/lib/cfunc.c", SRC_DIR + "/wrapped.pyx"],
                  libraries=[],
                  include_dirs=[np.get_include()],
                  extra_compile_args=extra_compile_args,
                  extra_link_args=extra_link_args)


EXTENSIONS = [ext_1]

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
          packages=PACKAGES,
          zip_safe=False,
          name=NAME,
          version=VERSION,
          description=DESCR,
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license=LICENSE,
          cmdclass={"build_ext": build_ext},
          ext_modules=EXTENSIONS
          )
