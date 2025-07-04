from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
setup(
    name='pairs3d',
    version='1.1',
    description='Stereo image pair sorter using timestamp and perceptual similarity',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='tiMaxal',
    py_modules=['pairs3d'],
    install_requires=['Pillow', 'imagehash'],
    entry_points={
        'console_scripts': [
            'pairs3d-cli = pairs3d:main',
        ],
        'gui_scripts': [
            'pairs3d = pairs3d:main',
        ],
    },
)
