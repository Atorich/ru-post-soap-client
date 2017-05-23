from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.rst'), 'r') as f:
    long_description = f.read()


with open(path.join(here, 'VERSION'), 'r') as f:
    version = f.read().strip()


setup(
    name='ruspost-soap-client',
    version=version,
    description='Implementation of Russian Post SOAP Tracking API',
    long_description=long_description,
    url='https://github.com/qnub/ru-post-soap-client',
    author='Vadim Lopatyuk',
    license='LGPL v3',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'

        'Environment :: Other Environment',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',  # noqa

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='rupost ruspost tracking api',
    install_requires=['suds-jurko'],
    packages=find_packages(),
    include_package_data=True,
)
