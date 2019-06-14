from setuptools import setup, find_packages
import sys, os.path

# Don't import gym module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pytorch_tensorflow_forecast_ml'))

VERSION = 0.1

setup(name='pytorch_tensorflow_forecast_ml',
      version=VERSION,
      description='General repo for testing / benchmarking different machine learning models for continuous data.',
      url='https://github.com/josiahls/PyTorchTensorflowForecastML',
      author='Josiah Laivins',
      author_email='jlaivins@uncc.edu',
      license='',
      packages=[package for package in find_packages()
                if package.startswith('pytorch_tensorflow_forecast_ml')],
      zip_safe=False,
      install_requires=['numpy', 'torch', 'tensorboardX', 'namedlist', 'pytest', 'torchvision', 'pandas', 'matplotlib',
                        'sklearn'
                        ]
)