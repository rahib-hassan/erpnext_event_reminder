from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in event_notification/__init__.py
from event_notification import __version__ as version

setup(
	name="event_notification",
	version=version,
	description="Alerts users before and after events.",
	author="Rahib",
	author_email="rahibhassan.10@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
