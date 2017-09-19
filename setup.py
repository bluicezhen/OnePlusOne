import ast
import re
from setuptools import find_packages, setup

# To import Niuniu.__version, I copied some code from
# https://raw.githubusercontent.com/pallets/werkzeug/master/setup.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('Niuniu/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))

setup(
    name='Niuniu',
    version=version,
    description='A web RESTFul framework simple as 1+1',
    long_description=open('README.md', 'rt').read(),
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
    packages=find_packages(exclude=['Niuniu']),
    install_requires=['Werkzeug'],
    python_requires=">=3.6, <4"
)
