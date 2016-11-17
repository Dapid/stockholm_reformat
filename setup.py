# -*- coding: utf8 -*-
import setuptools
from setuptools import setup
from setuptools.extension import Extension

ext = Extension('stockholm_reformat.creformat',
                sources=['stockholm_reformat/creformat.c'],
                extra_compile_args=['-O2', '-mtune=native', '-funroll-loops',
                                    '-fpic'])
setup(name='stockholm_reformat', version='0.3.1',
      ext_modules=[ext],
      description='Fast Stockholm to other formats Multiple Sequence Alignment reformater.',
      url='https://github.com/Dapid/stockholm_reformat',
      author='David Menéndez Hurtado',
      author_email='davidmenhur@gmail.com',
      license='BSD 3-clause',
      packages=setuptools.find_packages(),
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['bin/stockholm_to_a3m', 'bin/stockholm_to_fasta', 'bin/stockholm_to_aln'],
      classifiers=['Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Cython',
                   'Programming Language :: Python :: Implementation :: CPython',
                   'Topic :: Scientific/Engineering :: Bio-Informatics',
                   'Intended Audience :: Science/Research',
                   'Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: BSD License']
    )
