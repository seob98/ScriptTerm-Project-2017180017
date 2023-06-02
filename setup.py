#from distutils.core import setup

#setup(name='honing',
#      version='1.0',
#      py_modules=['Character', 'ChatBot', 'Equipment', 'HoningMat', 'LostArk', 'SearchEngine'])

from setuptools import setup, find_packages
import glob

image_files = glob.glob('image/*')

setup(
    name='honing',
    version='1.0',
    packages=find_packages(),
    py_modules=['Character', 'ChatBot', 'Equipment', 'HoningMat', 'LostArk', 'SearchEngine'],
    include_package_data=True,
    package_data={'': image_files}
)