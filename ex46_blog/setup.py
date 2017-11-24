try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'MorePy Blog',
    'author': 'Zed A. Shaw',
    'url': '',
    'download_url': '',
    'author_email': 'help@learncodethehardway.org',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['blog'],
    'scripts': ['bin/blog'],
    'name': 'blog'
}

setup(**config)

