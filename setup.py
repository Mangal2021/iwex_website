from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in iwex/__init__.py
from iwex import __version__ as version

setup(
	name="iwex",
	version=version,
	description="Iwex site ",
	author="Upcode Nepal",
	author_email="rock.team.381@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
