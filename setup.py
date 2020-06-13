import setuptools

setuptools.setup(
    name="telegramscraper", # Replace with your own username
    version="0.0.1",
    author="Hekuran Islamaj",
    author_email="hekuran.islamai@gmail.com",
    description="telegram scrape and send sms to user and groups",
    long_description="Scraper for telegram users",
    long_description_content_type="text/markdown",
    scripts=['setup_script'],
    install_requires=[
        'cython>=0.28',
        'pandas>=1.0.4',
        'numpy>=1.8.2',
        'configparser==3.2.0r1',
        'mysql-connector-python>=8.0.17',
        'requests[socks]>=2.22.0',
        'stem>=1.7.1',
        'urllib3>=1.25.7',
        'telethon>=1.14.0'
    ],
    extras_require={
        'dev': [
            'mock>=3.0.5',
            'pylint>=2.4.4',
            'pytest>=5.3.2',
            'tox>=3.14.3',
            'timeout-decorator>=0.4.1'
        ]
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        'telegramscraper': ['config.data'],
    },
    python_requires='>=3.7',
)