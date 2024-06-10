from setuptools import setup

setup(name="microbitlib",
      version='0.1',
      description="A library for the BBC micro:bit",
      url="github.com/CompSciSoc/microbitlib",
      author="CompSciSoc",
      author_email="jonah@rowlinson.eu",
      license="MIT",
      packages=["microbitlib"],
      install_requires=["pyserial"],
      zip_safe=False
)
