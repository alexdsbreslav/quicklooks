from setuptools import setup

setup(name='mpl_styled',
      version='0.1',
      description='A wrapper on matplotlib that facilitates fast/easy and attractive visualizations for exploratory data analysis.',
      url='http://github.com/storborg/funniest',
      author='Alexander Breslav',
      author_email='alexdsbreslav@gmail.com',
      packages=['mpl_styled'],
      install_requires = [
        'numpy',
        'pandas',
        'matplotlib',
        'datetime'
      ],
      include_package_data = True,
      zip_safe=False)
