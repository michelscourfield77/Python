from setuptools import setup, find_packages

setup(
    name="mon_calculateur",
    version="0.1.0",
    author="Michel Scourfield",
    description="Un module pour évaluer des expressions mathématiques et analyser les erreurs",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)




