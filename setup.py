#!/usr/bin/env python

from setuptools import setup
import os

dir = os.path.dirname(__file__)
path_to_readme = os.path.join(dir, "README.md")
version = "0.0.4"
readme = open(path_to_readme).read(-1)

classifiers = [
'Development Status :: 5 - Production/Stable',
'Environment :: Console',
'Environment :: No Input/Output (Daemon)',
'Intended Audience :: End Users/Desktop',
'Intended Audience :: System Administrators',
'License :: OSI Approved :: GNU General Public License (GPL)',
'Operating System :: POSIX :: Linux',
'Programming Language :: Python :: 2 :: Only',
'Programming Language :: Python :: 2.7',
'Topic :: Utilities',
]

setup(
	name = 'needs-restart',
	version=version,
	description = 'A program to discover services that need restarting',
	long_description = readme,
	author='Manuel Amador (Rudd-O)',
	author_email='rudd-o@rudd-o.com',
	license="GPL",
	url = 'http://github.com/Rudd-O/needs-restart',
	package_dir=dict(),
	classifiers = classifiers,
	scripts = ["needs-restart"],
	keywords = "systemd services",
	zip_safe=False,
)
