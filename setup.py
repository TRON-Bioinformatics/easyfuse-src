from setuptools import find_packages, setup
import easy_fuse


# parses requirements from file
with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("README.md", "r") as f:
    long_description = f.read()

# Build the Python package
setup(
    name="easy_fuse",
    version=easy_fuse.__version__,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "easy-fuse=easy_fuse.processing:main"
        ],
    },
    author_email="patrick.sorn@tron-mainz.de",
    author="TRON - Translational Oncology at the University Medical Center of the Johannes Gutenberg University Mainz "
           "- Computational Medicine group",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    requires=[],
    install_requires=required,
    setup_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Programming Language :: Python :: 3.7",
    ],
)