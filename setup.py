from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "selenium",
    ],
    entry_points={
        'console_scripts': [
            'your_command=your_module:main_function',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your project",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/jstutz4/YSA_stake_names",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
