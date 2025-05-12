from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'quicklooks',         # How you named your package folder (MyLib)
  packages = ['quicklooks'],   # Chose the same as "name"
  version = '1.0.7',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'quicklook is a Python package for visualizing data quickly using matplotlib.',   # Give a short description about your library
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  include_package_data=True, #fonts
  author = 'Alex Breslav',                   # Type in your name
  author_email = 'alexdsbreslav@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/alexdsbreslav/quicklooks',   # Provide either the link to your github or to your website
  keywords = ['matplotlib', 'data-visualization', 'python'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'matplotlib',
          'pandas',
          'datetime',
          'seaborn'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3.9',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
  ],
)
