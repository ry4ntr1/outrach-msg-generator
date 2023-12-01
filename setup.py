from setuptools import setup, find_packages

setup(
    name="invitAI",
    version="0.1.0",
    description="A brief description of your project",
    author="Ryan Tri",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/your_project_name",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask==2.1.1",
        "openai==0.27.0",
        "PyPDF2==1.27.9",
        "Werkzeug==2.1.1",
        "pdfminer.six==20201018",
        "python-dotenv==0.19.2",
        "spacy==3.2.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
