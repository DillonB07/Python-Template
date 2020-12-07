import setuptools

# Reads README.md and sets it to long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with package name
    version="0.0.1", # Change for every update
    author="Example Author", # Your name / username
    author_email="author@example.com", # Email
    description="A small example package", # Small Description
    long_description=long_description, # README.md
    long_description_content_type="text/markdown", # Specifies that it is a markdown file
    url="https://github.com/pypa/sampleproject", # Github / Website URL
    packages=setuptools.find_packages(), # Which packages to include. Setuptools automatically does this.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # Edit based on https://pypi.org/classifiers/
    python_requires='>=3.8', # Python version. This package was developed for Python 3. We cannot say whether it will still work for previous versions.
)
