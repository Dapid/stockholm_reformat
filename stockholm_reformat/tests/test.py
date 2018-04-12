import os
from nose.exc import SkipTest

from stockholm_reformat import parse_a3m, parse_fasta, parse_aln

def assert_equal_a3m(ref_file, check_file):
    new = dict()
    ref = dict()

    check = open(check_file)
    for line in check:
        new[line.strip()] = next(check).strip()
    check.close()

    _this = []
    _head = None
    for line in open(ref_file):
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

    assert len(ref) == len(new)


def assert_equal_files(one, other):
    one_f = open(one)
    other_f = open(other)
    for line1, line2 in zip(one_f, other_f):
        if not line1.strip() == line2.strip():
            print(line1)
            print(line2)
            raise AssertionError
    # Check we are at the end of the file:
    assert one_f.read() == ''
    assert other_f.read() == ''

def assert_equal_aln(ref_file, check_file):
    one = open(ref_file).readlines()
    other = open(check_file).readlines()
    one.sort()
    other.sort()

    assert one == other

def test_purepython_a3m():
    parse_a3m('data/sequence.fa.sto', 'data/output.a3m')
    assert_equal_a3m('data/sequence.fa.a3m','data/output.a3m')
    os.unlink('data/output.a3m')


def test_cython_a3m():
    try:
        from stockholm_reformat.creformat import cparse_a3m
    except ImportError:
        raise SkipTest('Compiled version unavailable')

    cparse_a3m('data/sequence.fa.sto', 'data/output_c.a3m')
    assert_equal_a3m('data/sequence.fa.a3m','data/output_c.a3m')

    parse_a3m('data/sequence.fa.sto', 'data/output_p.a3m')

    assert_equal_a3m('data/output_p.a3m', 'data/output_c.a3m')
    assert_equal_files('data/output_p.a3m', 'data/output_c.a3m')

    os.unlink('data/output_c.a3m')
    os.unlink('data/output_p.a3m')


def test_purepython_fasta():
    parse_fasta('data/sequence.fa.sto', 'data/output.fasta')
    assert_equal_a3m('data/sequence.fa.fasta','data/output.fasta')
    os.unlink('data/output.fasta')


def test_cython_fasta():
    try:
        from stockholm_reformat import cparse_fasta
    except ImportError:
        raise SkipTest('Compiled version unavailable')

    cparse_fasta('data/sequence.fa.sto', 'data/output_c.fasta')
    assert_equal_a3m('data/sequence.fa.fasta','data/output_c.fasta')

    parse_fasta('data/sequence.fa.sto', 'data/output_p.fasta')
    assert_equal_a3m('data/output_p.fasta', 'data/output_c.fasta')
    assert_equal_files('data/output_p.fasta', 'data/output_c.fasta')

    os.unlink('data/output_p.fasta')
    os.unlink('data/output_c.fasta')


def test_purepython_aln():
    parse_aln('data/sequence.fa.sto', 'data/output.aln')
    assert_equal_aln('data/sequence.fa.aln','data/output.aln')
    os.unlink('data/output.aln')


def test_cython_aln():
    try:
        from stockholm_reformat import cparse_aln
    except ImportError:
        raise SkipTest('Compiled version unavailable')

    cparse_aln('data/sequence.fa.sto', 'data/output_c.aln')
    assert_equal_aln('data/sequence.fa.aln','data/output_c.aln')

    parse_aln('data/sequence.fa.sto', 'data/output_p.aln')
    assert_equal_files('data/output_p.aln', 'data/output_c.aln')

    os.unlink('data/output_p.aln')
    os.unlink('data/output_c.aln')


if __name__ == '__main__':
    import nose
    nose.main()
