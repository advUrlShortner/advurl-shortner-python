from setuptools import find_packages, setup

# read the contents of your README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'advurl_shortner',
  packages = find_packages(include=["advurl_shortner"]),
  version = '1.0.0',
  license='MIT',
  description = 'Python Library to help you short urls  using advanced options. Multiple domains supported',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Paul Jakobski',
  url = 'https://github.com/advUrlShortner/advurl-shortner-python',
  keywords = ['url', 'shorten', 'url_shortner','API'],
  install_requires=["requests>=2.23.0"],
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*'
)
