from setuptools import setup

setup(name='quicklook',
      version='0.1',
      description='A wrapper on matplotlib that facilitates fast/easy and attractive visualizations for exploratory data analysis.',
      url='https://github.com/alexdsbreslav/quicklook',
      author='Alexander Breslav',
      author_email='alexdsbreslav@gmail.com',
      packages =['quicklook'],
      package_data = {'quicklook' : ['fonts/Futura.ttc', 'fonts/SourceSansPro-Black.ttf', 'fonts/SourceSansPro-Regular.ttf']},
      install_requires = [
        'numpy',
        'matplotlib',
      ],
      include_package_data = True,
      zip_safe=False)
