try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description:': 'Automated Testing',
    'author': 'IggiRex',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author-email': 'iggirex@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47 testing automation'
}

setup(**config)
