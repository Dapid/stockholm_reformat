from reformat import parse_a3m, parse_fasta
try:
    from creformat import cparse_a3m, cparse_fasta
except ImportError:
    pass
__version__ = '0.2.dev1'
