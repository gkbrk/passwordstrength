from setuptools import *

kwargs = {
	'name' : 'passwordstrength',
	'version' : '0.1',
	'description' : 'A password strength checker.',
	'entry_points' : {'console_scripts' : ['passwordstrength=passwordstrength.passwordstrength:main']},
	'packages' : ['passwordstrength'],
	'package_data' : {'passwordstrength': ['english']},
	'include_package_data' : True,
}

setup(**kwargs)
