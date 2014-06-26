from setuptools import *

kwargs = {
	"description" : "A password strength checker.",
	"entry_points" : {"console_scripts" : ["passwordstrength=passwordstrength.passwordstrength:main"]},
	"name" : "passwordstrength",
	"packages" : ["passwordstrength"],
}

setup(**kwargs)
