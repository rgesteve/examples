import sys, os, json
import platform
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

config = json.load(open("config.json"))
__eigen_lib_dir__ = config["path_to_eigen"]

IS_WINDOWS = (platform.system() == 'Windows')
IS_LINUX = (platform.system() == 'Linux')

if IS_WINDOWS:
    #extra_compile_args = ['/Zi']
    #extra_link_args = ['/DEBUG', '/PDB:"%s"' % pdb_file]
    extra_link_args = ['/DEBUG:FULL']
    extra_compile_args = ['/Zi', '/Od']
else:
    extra_link_args = []
    extra_compile_args = ['-g']    

class get_pybind_include(object) :
    """Helper class to determine the pybind11 include path.
    By wrapping it inside a class we postpone importing pybind11
    until it is actually installed, so that the `get_include()`
    method can be invoked.
    """

    def __init__(self, user=False) :
        self.user = user
    
    def __str__(self) :
        import pybind11
        return pybind11.get_include(self.user)

ext_modules = [Extension(
    'montecarlopi',
    ['src/MonteCarloPi.cpp'],
    include_dirs = [
        get_pybind_include(user = True),
        get_pybind_include()
    ],
    language = 'c++',
    extra_compile_args = extra_compile_args,
    extra_link_args = extra_link_args
)]

setup(
    name = 'montecarlopi',
    version = '0.0.1',
    author = 'R. G. Esteves',
    author_email = 'rgesteves@gmail.com',
    description = 'Estimate pi using Monte Carlo bound with pybind11',
    ext_modules = ext_modules,
    install_requires = ['pybind11>=2.2']
)