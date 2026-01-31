from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECOMMENDER",
    version="0.3",
    author="Kunal-M",
    packages=find_packages(),
    install_requires = requirements,
)