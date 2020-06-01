from setuptools import setup, find_packages

setup(
    name='snotify',
    version='1.0',
    description='Simple notification tool for Spotifyd.',
    author='teegre',
    packages=find_packages(),
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'snotify=snotify:main',
        ],
    },
    platforms = ['Linux'],
    license='LICENSE.txt',
)
