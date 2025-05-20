from setuptools import setup, find_packages

setup(
    name='cryptolib',
    version='0.1.0',  
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python library for blockchain utilities',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cryptolib',
    packages=find_packages(),
    install_requires=[
        'flask==0.5'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
