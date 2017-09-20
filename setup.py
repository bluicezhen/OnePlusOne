import ast
import re
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))
_version_re = re.compile('__version__\s+=\s+(.*)')
with open(here + '/Niuniu/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))

setup(
    name='Niuniu',
    version=version,
    description='A web RESTFul framework simple as 1+1',
    long_description=open(here +'/README.rst', 'rt').read(),
    url='https://github.com/bluicezhen/Niuniu',
    author='Bluice Zhen',
    author_email='bluice.zhen@gmail.com',
    license='GPL',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='web framework werkzeug',
    packages=['Niuniu'],
    install_requires=['Werkzeug'],
    python_requires=">=3.6, <4"
)
