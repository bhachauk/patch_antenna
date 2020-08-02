from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='patch_antenna',
      version='0.0.6',
      long_description=long_description,
      long_description_content_type='text/markdown',
      description='A simple patch antenna design library',
      url='https://github.com/bhanuchander210/design_patch_antenna.git',
      author='Bhanuchander Udhayakumar',
      author_email='bhanuchander210@gmail.com',
      license='MIT',
      packages=['patch_antenna'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['scipy']
      )