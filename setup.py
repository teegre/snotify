from setuptools import setup, find_packages

setup(
    name='snotify',
    version='0.5.1',
    description='Simple notification tool and basic playback controller for Spotifyd.',
    author='teegre',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'spotipy>=2.4.4',
    ],
    entry_points={
        'console_scripts': [
            'snotify=snotify:main',
        ],
    },
    platforms = ['Linux'],
    license='LICENSE.txt',
)
