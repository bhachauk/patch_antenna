from setuptools import setup

setup(name='patch_antenna',
      version='0.0.1',
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