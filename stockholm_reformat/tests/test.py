import os
from nose.exc import SkipTest

from stockholm_reformat import parse_a3m, parse_fasta

def assert_equal_a3m(ref_file, check_file):
    new = dict()
    ref = dict()

    check = open(check_file)
    for line in check:
        new[line.strip()] = check.next().strip()
    check.close()

    _this = []
    _head = None
    for line in ref_file:
        if line.startswith('>'):
            sequence = ''.join(_this)
            ref[_head] = sequence

            _head = line.strip()
            _this = []
        else:
            _this.append(line.strip())
    ref[_head] = ''.join(_this)
    del ref[None]

    for ky in ref.keys():
        assert ref[ky] == new[ky]


def test_purepython_a3m():
    parse_a3m('data/sequence.fa.sto', 'data/output.a3m')
    assert_equal_a3m('data/sequence.fa.a3m','data/output.a3m')
    os.unlink('data/output.a3m')


def test_cython_a3m():
    try:
        from stockholm_reformat import cparse_a3m
    except ImportError:
        raise SkipTest('Compiled version unavailable')

    cparse_a3m('data/sequence.fa.sto', 'data/output_c.a3m')
    assert_equal_a3m('data/sequence.fa.a3m','data/output_c.a3m')

    parse_a3m('data/sequence.fa.sto', 'data/output_p.a3m')
    assert_equal_a3m('data/output_p.a3m', 'data/output_c.a3m')

    os.unlink('data/output_c.a3m')
    os.unlink('data/output_p.a3m')

def test_purepython_fasta():
    parse_fasta('data/sequence.fa.sto', 'data/output.fasta')
    assert_equal_a3m('data/sequence.fa.fasta','data/output.a3m')
    os.unlink('data/output.fasta')
