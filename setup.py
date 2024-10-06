from setuptools import setup, find_packages

setup(
    name="privacy_monitor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pyshark',
    ],
    entry_points={
        'console_scripts': [
            'privacy_monitor=privacy_monitorr.main:main',
        ],
    },
)