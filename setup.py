import atexit
from setuptools import setup
from setuptools.command.install import install

def post_install_msg():
    print("NOTE: make sure to install Tkinter, Pillow, and UnDotum.")
    print("NOTE: for Ubuntu 22.04, try these commands to install them.")
    print("NOTE:  $ sudo apt install python3-tk")
    print("NOTE:  $ sudo apt install python3-pil.imagetk")
    print("NOTE:  $ sudo apt install fonts-unfonts-core")

class PostInstallCommand(install):
    def __init__(self, *args, **kwargs):
        super(PostInstallCommand, self).__init__(*args, **kwargs)
        atexit.register(post_install_msg)

with open("README.md", 'r') as f:
    readme = f.read()

with open("LICENSE", 'r') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='eng-to-hangul',
    version='0.1',
    description='English sentence to naturally-sounding (augmented) Hangul notation',
    author='Gwangmu Lee',
    author_email='iss300@gmail.com',
    url='https://github.com/gwangmu/eng-to-hangul',
    long_description=readme,
    license=license,
    packages=['eng_to_hangul'],
    scripts=['scripts/eng-to-hangul'],
    install_requires=requirements,
    cmdclass={'install': PostInstallCommand},
)
