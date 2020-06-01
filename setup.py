from setuptools import setup

setup(
    name='snotify',
    version='1.0',
    description='Simple notification tool for Spotifyd.',
    author='teegre',
    url='https://github.com/teegre/snotify',
    packages=['snotify'],
    entry_points={'console_scripts': ['snotify=snotify:main',]},
    python_requires='>=3.8',
    platforms = ['Linux'],
    license='MIT',
)

