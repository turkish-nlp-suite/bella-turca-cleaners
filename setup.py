from setuptools import setup, find_packages

setup(
    name="bella_cleaner",
    version="1.0.0",
    author="Duygu Altinok",
    author_email="duygu.altinok12@gmail.com",
    description="Text cleaning and document processing code for Bella Turca",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/DuyguA/turkish-corpus-cleaner",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pyyaml",
    ],
)
