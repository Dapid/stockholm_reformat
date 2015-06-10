from distutils.core import setup
from distutils.extension import Extension

module = 'stockholm_reformat'
ext = Extension('stockholm_reformat.creformat',
                sources=['stockholm_reformat/creformat.c'],
                extra_compile_args=['-O2', '-mtune=native', '-funroll-loops',
                                    '-fpic', '-flto', '-g0'])

setup(name=module, version='0.1',
      ext_modules=[ext],
      description='Stockholm to A3M multiple sequence alignment reformater',
      url='https://github.com/Dapid/stockholm_reformat',
      author='David Men\'endez Hurtado',
      license='BSD 3-clause',
      packages=['stockholm_reformat'],
      test_suite='nose.collector',
      tests_require=['nose']
    )