from setuptools import setup
import tokenhandler

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='tokenhandler',
    version=tokenhandler.__version__,
    description='Token Handler for the SALTED broker architecture.',
    url='https://github.com/SALTED-Project/TokenHandler',
    author='Maren Dietzel',
    author_email='maren.dietzel@kybeidos.de',
    license='',
    packages=['tokenhandler'],
    install_requires=required
)