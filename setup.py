from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

HYPEN_E_DOT = '-e .'

def get_requirements(filepath: str):
    requirements = []
    with open(filepath, "r") as f:
        requirements = [req.strip() for req in f.readlines()]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

__version__ = "0.0.1"
AUTHOR_USER_NAME = "lazygeniusbilal"
AUTHOR_EMAIL = "bilal.ahmed38980@gmail.com"
SRC_REPO = "MLProject"
REPO_NAME = "ELASTICPREMIUMPREDICTION"

setup(
    name=SRC_REPO,
    version=__version__,
    long_description=long_description,
    description="This is a project for insurance elasticity premium prediction.",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    url=f"https://www.github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements_dev.txt")
)
