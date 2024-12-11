import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

# Package Metadata
REPO_NAME = "Chest-Cancer-Classification-Project"
AUTHOR_USER_NAME = "ashaduzzaman-sarker"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "ashaduzzaman2505@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for chest cancer classification using computer vision",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Fixed typo
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Specify minimum Python version
    install_requires=[
        "tensorflow>=2.12.0",
        "numpy>=1.21.6",
        "pandas>=1.3.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.2",
        "dvc>=2.20.0",
        "mlflow==2.2.2",
        "gdown>=4.5.0",
        "PyYAML>=6.0",
        "tqdm>=4.64.0",
        "Flask>=2.2.0",
        "Flask-Cors>=3.0.0",
    ],  # Added dependencies for better out-of-the-box use
    include_package_data=True,  # Ensures non-code files like README.md are included
)
