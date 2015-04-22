# -*- coding: utf-8 -*-

from distutils.core import setup


long_description = """
txldapv2 is a Twisted wrapper for python-ldap.
"""

setup(
    name='txldapv2',
    version='0.2.0',
    description='Twisted wrapper for python-ldap',
    long_description=long_description.strip(),
    author='Silas Sewell',
    author_email='silas@sewell.ch',
    maintainer='Richard Kuesters',
    maintainer_email='rkuesters@gmail.com',
    license='MIT',
    url='https://github.com/vltr/txldapv2',
    py_modules=['txldapv2'],
    install_requires=[
        'twisted',
        'python-ldap'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
