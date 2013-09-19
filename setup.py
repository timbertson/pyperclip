from os.path import join, dirname
from setuptools import setup

version = open(join(dirname(__file__), "VERSION"), "r").read().strip()

setup(name='pyperclip',
      version=version,
      description='A cross-platform clipboardmodule for Python. (only handles plain text for now)',
      author='Al Sweigart',
      author_email='al@coffeeghost.net',
      url='https://github.com/gfxmonk/pyperclip',
      py_modules=['pyperclip'],
      install_requires=['which'],
      license='BSD',
      classifiers=(
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
          )
      )

