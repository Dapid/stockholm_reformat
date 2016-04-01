import os

from stockholm_reformat import parse_a3m, parse_fasta, parse_aln
from stockholm_reformat import cparse_a3m, cparse_fasta, cparse_aln


def run_a3m():
    parse_a3m('data/sequence.fa.sto', 'data/output_p.a3m')
    cparse_a3m('data/sequence.fa.sto', 'data/output_c.a3m')
    os.unlink('data/output_c.a3m')
    os.unlink('data/output_p.a3m')


def run_fasta():
    parse_fasta('data/sequence.fa.sto', 'data/output_p.fasta')
    cparse_fasta('data/sequence.fa.sto', 'data/output_c.fasta')
    os.unlink('data/output_c.fasta')
    os.unlink('data/output_p.fasta')


def run_aln():
    parse_aln('data/sequence.fa.sto', 'data/output_p.aln')
    cparse_aln('data/sequence.fa.sto', 'data/output_c.aln')

    os.unlink('data/output_p.aln')
    os.unlink('data/output_c.aln')


if __name__ == '__main__':
    run_a3m()
    run_aln()
    run_fasta()
