from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='poetryanalysis',
      version='0.3',
      description='Analyze rhyme scheme, meter and form of poems',
      long_description=readme(),
      author='Warren Galyen',
      url='http://www.mechanikadesign.com',
      license='MIT',
      packages=['poetryanalysis'],
      install_requires=['python-levenshtein'],
      include_package_data=True
)
