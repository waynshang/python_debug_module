from setuptools import setup, find_packages

classifier = [
  'Development Status :: Production',
  'Intended Audience :: Developers',
  'License :: OSI Approved :: MIT License',
  'programming Language :: Python :: 3.8'
]

setup(
  name='debuggerModule',
  version='0.3',
  description='A package for create debug modules',
  long_description=open('README.md').read(),
  author='Wayne Shang',
  author_email='wayne18308@gmail.com',
  license='MIT',
  classifier=classifier,
  keywords='debug',
  packages=find_packages(),
  install_requires=['']

)