# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='pyedid',
    version='0.1.0',
    description='Python library to parse extended display identification data (EDID)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jojonas/pyedid',
    author='Jonas Lieb',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    package_dir={'': '.'},
    packages=find_packages(where='.'),
    python_requires='>=3.5, <4',
    package_data={ 
        'database': ['pyedid/pnp_ids.csv'],
    },
    entry_points={
        'console_scripts': [
            'pyedid=pyedid.edid:main',
        ],
    }
)
