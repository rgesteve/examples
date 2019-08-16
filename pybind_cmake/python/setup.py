from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import setuptools

import sys, os

def find_pybind_headers_dir():
    pass

def parallelCCompile():
    pass

def has_flag():
    pass

def cpp_flag():
    pass

def add_platform_specific_link_args():
    pass

class BuildExt(build_ext):
    """A custom build extension for adding compiler-specific options"""
    def _add_extra_compile_arg(self):
        pass

    def build_extensions(self):
        """Build extension providing extra compiler flags."""
        pass

sources = [
    'pymonte/pymonte.cpp'
    ]

ext_modules = [
    Extension('_pymc',
              sources = sources)
]

setup(
    name        = "pymonte",
    description = "Scaffolding for a cmake-based Python extension",
    author      = "Intel",
    license     = "ISC",
    ext_modules = ext_modules,
)
