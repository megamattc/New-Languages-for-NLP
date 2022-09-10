
from setuptools import setup
setup(
    name="meow",
    entry_points={
        "spacy_languages": ["meow = meow:Meow"],
    }
)
