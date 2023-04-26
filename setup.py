from setuptools import find_packages, setup

setup (
	   name="sysvis",
	   version="0.0.1",
	   packages=find_packages(),
	   include_package_data=True,
       py_modules=["sysvis.py"],
	   install_requires=[
		   'click',
           'psutil'
		   # Any other required packages for pip to install.
	   ],
	   entry_points={
		   "console_scripts": [
			   "sysvis = sysvis.sysvis:run",
		   ],
	   },
)