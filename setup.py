import os
from setuptools import find_packages
from distutils.core import setup

current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
	name='annhub_python',
	packages=find_packages('.'),
	version='0.1.0',
	description='ANNHUB Python library, which can be used to generate web controller to serve ANNHUB model immediately',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='ARI Technology',
	author_email='dung.ut@ari.com.vn',
	url='https://github.com/ans-ari/annhub-python',
	download_url='https://github.com/ans-ari/annhub-python',
	install_requires=[
        "fastapi==0.68.1",
        "uvicorn ==0.11.1",
        "pydantic",
        "requests==2.22.0",
        "loguru==0.4.0",
        "pytest==6.2.4",
        "joblib==1.0.1"
    ]
)
