from __future__ import absolute_import
from .reformat import parse_a3m, parse_fasta, parse_aln
try:
    from .creformat import cparse_a3m, cparse_fasta, cparse_aln
except ImportError:
    pass

__version__ = '0.3'
