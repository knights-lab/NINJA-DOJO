from setuptools import setup
from glob import glob
import os

__author__ = "Knights Lab"
__copyright__ = "Copyright (c) 2016--, %s" % __author__
__credits__ = ["Benjamin Hillmann", "Dan Knights", "Gabe Al-Ghalith", "Tonya Ward", "Pajua Vangay"]
__email__ = "hillmannben@gmail.com"
__license__ = "GPL"
__maintainer__ = "Benjamin Hillmann"
__version__ = "0.0.1-dev"

long_description = ''

setup(
    name='ninja_dojo',
    version=__version__,
    packages=['ninja_dojo'],
    url='',
    license=__license__,
    author=__author__,
    author_email=__email__,
    description='',
    test_suite='nose.collector',
    long_description=long_description,
    # scripts=glob(os.path.join('scripts', '*py')),
    entry_points={
        'console_scripts': [
            'extract_ncbi_tid_from_mp2_gold = ninja_dojo.scripts.sim_mp2_gold:extract_ncbi_tid',
        ]
    },
    keywords='',
    install_requires=['click', 'networkx', 'nose', 'pandas', 'bcolz', 'skbio']
)