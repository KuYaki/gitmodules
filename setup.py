from distutils.core import setup
import gitmodules

setup(
  name='gitmodules',
  packages=['gitmodules'],
  version=gitmodules.__version__,
  license='MIT',
  description='Import this module to use gitmodules in Python projects without headache',
  long_description='This project was developed to avoid problems with gitmodules importing in Python projects.',
  author=gitmodules.__author__,
  author_email='kuzma.yakimets@huawei.com',
  url='https://github.com/kuyaki/gitmodules',
  download_url='https://github.com/kuyaki/gitmodules/archive/v0.0.2.tar.gz',
  keywords=['git', 'submodules', 'submodule', 'module', 'gitmodules', 'gitmodule', 'python', 'import'],
  classifiers=[
    'Development Status :: 3 - Alpha',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
