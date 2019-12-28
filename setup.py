from setuptools import setup, find_packages

setup(
    name='snotify',
    version='0.4.0',
    description='Simple notification tool and playback controller for Spotifyd.',
    author='teegre',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'spotipy>=2.4.4',
        'spotify-token>=0.1.0',
    ],
    entry_points={
        'console_scripts': [
            'snotify=snotify:main',
        ],
    },
    platforms = ['Linux'],
    license='LICENSE.txt',
)
