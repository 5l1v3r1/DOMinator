from setuptools import setup
setup(
    name = 'dominator',
    version = '0.1.0',
    packages = ['dominator'],
    entry_points = {
        'console_scripts': [
            'dominator = dominator.__main__:main'
        ]
    })