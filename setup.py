from setuptools import setup, find_packages

setup(
    name="curtaon-automacoes",
    version="1.0.0",
    description="Framework de automação de testes para o CurtaON",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    packages=find_packages(include=['utils', 'utils.*']),
    install_requires=[
        "selenium>=4.15.2",
        "pytest>=7.4.3",
        "pytest-html>=4.1.1",
        "webdriver-manager>=4.0.1",
        "python-dotenv>=1.0.0",
        "pytest-xdist>=3.3.1",
        "pytest-rerunfailures>=12.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Testing",
    ],
    python_requires=">=3.8",
) 