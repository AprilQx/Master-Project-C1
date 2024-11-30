from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(
        "dual_autodiff_x.dual",
        ["dual_autodiff_x/dual.pyx"],
        include_dirs=[numpy.get_include()] # This is required to include the numpy headers
    )
]

setup(
    name="dual_autodiff_x",
    version="0.1.0",
    packages=["dual_autodiff_x"],
    ext_modules=cythonize(extensions),
    zip_safe=False,
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.20.0",
    ],
)