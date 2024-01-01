from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ask_the_wizard",
    version="0.0.1.rc1",
    description="Are you still thinking while coding or are you already Asking The Wizard? 🧙",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tizianerlenberg/ask_the_wizard",
    author="Andreas Menzel, Tizian Erlenberg",
    author_email="mail@andreas-menzel.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["python-dotenv~=1.0.0", "openai~=1.6.1", "requests~=2.31.0"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)