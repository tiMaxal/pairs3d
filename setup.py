from setuptools import setup

setup(
    name='pairs3d',
    version='1.0',
    description='Stereo image pair sorter using timestamp and perceptual similarity',
    author='tiMaxal',
    py_modules=['pairs3d'],
    install_requires=['Pillow', 'imagehash'],
    entry_points={
        'gui_scripts': [
            'pairs3d = pairs3d:main',
        ],
    },
)
