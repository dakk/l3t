# -*- coding: utf-8 -*-
# Copyright (C) 2019 Davide Gessa

from setuptools import find_packages
from setuptools import setup

setup(name='l3t',
	version='0.1',
	description='',
	author=['Davide Gessa'],
	setup_requires='setuptools',
	author_email=['gessadavide@gmail.com'],
	packages=[
		'l3t',
		'l3t.lmodules'
	],
	entry_points={
		'console_scripts': [
			'l3t=l3t.main:main',
		],
	},
	install_requires=open ('requirements.txt', 'r').read ().split ('\n'),
)