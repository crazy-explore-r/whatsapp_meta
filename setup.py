from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in whatsapp_meta/__init__.py
from whatsapp_meta import __version__ as version

setup(
	name="whatsapp_meta",
	version=version,
	description="Whatsapp Buisiness integration for Frappe",
	author="Ragul KM",
	author_email="developer.ragul@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
