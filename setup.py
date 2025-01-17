from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='matscholar',
    version='0.0.2',
    description='matscholar: a Python library for interacting with the Matscholar database.',
    long_description=readme,
    author='Materials Scholar Development Team',
    author_email='jdagdelen@lbl.gov, vahe@tshitoyan.com, lweston@lbl.gov',
    url='https://github.com/materialsintelligence/matscholar',
    license=license,
    packages=find_packages()
)
