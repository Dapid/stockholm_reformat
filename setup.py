# -*- coding: utf8 -*-
from setuptools import setup
from setuptools.extension import Extension

module = 'stockholm_reformat'
ext = Extension('stockholm_reformat.creformat',
                sources=['stockholm_reformat/creformat.c'],
                extra_compile_args=['-O2', '-mtune=native', '-funroll-loops',
                                    '-fpic'])

setup(name=module, version='0.3',
      ext_modules=[ext],
      description='Fast Stockholm to other formats Multiple Sequence Alignment reformater.',
      url='https://github.com/Dapid/stockholm_reformat',
      author='David Menéndez Hurtado',
      author_email='davidmenhur@gmail.com',
      license='BSD 3-clause',
      packages=['stockholm_reformat'],
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