from setuptools import setup

with open('README.md', 'r') as mdfile:
    des = mdfile.read()

setup(
    name='tf2-api',
    version='0.0.1',
    scripts=['tf2.py'],
    author="Hollo",
    author_email="hollo1234567890e@gmail.com",
    long_description=des,
    description='A simple api to get player stats for TF2',
    long_description_content_type="text/markdown",
    install_requires=[
        "requests==2.31.0"
    ],
    url="https://github.com/DevHollo/tf2-api/"
)