from glob import glob
from os.path import basename, sep
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="liat_ml_roberta",
    version="0.0.1",
    description="Multi-Launguage RoBERTa trained by RIKEN-AIP LIAT.",
    author="k141303",
    packages=["liat_ml_roberta", "liat_ml_roberta.tokenizers", "liat_ml_roberta.utils"],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=_requires_from_file("requirements.txt"),
)
