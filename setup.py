from distutils.core import setup
from distutils.extension import Extension

module = 'stockholm_reformat'
ext = Extension('stockholm_reformat.creformat',
                sources=['stockholm_reformat/creformat.c'],
                extra_compile_args=['-O2', '-mtune=native', '-funroll-loops',
                                    '-fpic', '-flto', '-g0'])

setup(name=module, version='0.1',
      ext_modules=[ext],
      description='Fast Stockholm to A3M Multiple Sequence Alignment reformater',
      url='https://github.com/Dapid/stockholm_reformat',
      author='David Men\'endez Hurtado',
      author_email='davidmenhur@gmail.com',
      license='BSD 3-clause',
      packages=['stockholm_reformat'],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['bin/stockholm_to_a3m'],
      zip_safe=True
    )