from setuptools import setup

setup(
    name='hypeline',
    version='0.1',
    py_modules=['hypeline'],
    install_requires=[
        'gspread',
        'dropbox',
        'requests',
        'pandas',
        'ftrack_api',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'hypeline = hypeline:main',
        ],
    },
)