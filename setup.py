import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chest-Disease-Classification"
AUTHOR_USER_NAME = "druvpat01"
SRC_REPO = "classifier"
AUTHOR_EMAIL = "patelddhhrruuvv@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN based classification.",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        'Bug Tracker': f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": 'src'},    # states that root -> "" is 'src'
    packages=setuptools.find_packages(where='src')  # automatatically detects all packages in 'src' using the folders with __init__.py 
)


# run command 'pip install -e .' for the setup.py