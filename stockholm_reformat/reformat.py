import os
from collections import defaultdict


def _validate_input(inputfile, outputfile):
    if isinstance(inputfile, basestring):
        # Pre-load the file in memory, if vmtouch is installed.
        os.system('vmtouch -qt {} & >/dev/null 2>/dev/null'.format(inputfile))

        input_ = open(inputfile)
        close_input = True

    elif isinstance(inputfile, file):
        input_ = inputfile
        close_input = False
    else:
        raise ValueError('inputfile should be a file name or a'
                         'file handler, got {} instead.'.format(type(inputfile)))

    if isinstance(outputfile, basestring):
        output = open(outputfile, 'w')
        close_output = True
    elif isinstance(outputfile, file):
        output = outputfile
        close_output = False
    else:
        raise ValueError('outputfile should be a file name or a'
                         'file handler, got {} instead.'.format(type(outputfile)))

    return input_, close_input, output, close_output


def parse_a3m(inputfile, outputfile):
    input_, close_input, output, close_output = _validate_input(inputfile, outputfile)

    data = defaultdict(list)
    reference_seq = []

    for line in input_:
        line = line.strip()
        if line and not line.startswith('#'):
            header, sequence = line.split()
            break

    while True:
        reference_seq.extend((s for s in sequence if s != '-'))
        index = [True if s != '-' else False for s in sequence]
        for line in input_:
            line = line.strip()
            if not line:
                break
            if not line.startswith('#'):
                try:
                    name, seq = line.split()
                    data[name].extend(s if i else s.lower() for s, i in zip(seq, index) if i or s != '-')
                except ValueError:
                    # End of file
                    pass

        try:
            header, sequence = input_.next().split()
        except StopIteration:
            break

    if close_input:
        input_.close()
    os.system('vmtouch -qe {} & >/dev/null 2>/dev/null'.format(inputfile))

    # Write to file
    output.write(''.join(('>', header, '\n')))
    output.write(''.join(reference_seq))
    output.write('\n')

    for name, seq in data.iteritems():
        output.write(''.join(('>', name, '\n')))
        output.write(''.join(seq))
        output.write('\n')

    if close_output:
        output.close()
    else:
        output.flush()


def parse_fasta(inputfile, outputfile):
    input_, close_input, output, close_output = _validate_input(inputfile, outputfile)

    data = defaultdict(list)
    reference_seq = []

    for line in input_:
        line = line.strip()
        if line and not line.startswith('#'):
            header, sequence = line.split()
            break

    while True:
        reference_seq.extend((s for s in sequence if s != '-'))
        index = [True if s != '-' else False for s in sequence]
        for line in input_:
            line = line.strip()
            if not line:
                break
            if not line.startswith('#'):
                try:
                    name, seq = line.split()
                    data[name].extend(s for s, i in zip(seq, index) if i)
                except ValueError:
                    # End of file
                    pass

        try:
            header, sequence = input_.next().split()
        except StopIteration:
            break

    if close_input:
        input_.close()
    os.system('vmtouch -qe {} & >/dev/null 2>/dev/null'.format(inputfile))

    # Write to file
    output.write(''.join(('>', header, '\n')))
    output.write(''.join(reference_seq))
    output.write('\n')

    for name, seq in data.iteritems():
        output.write(''.join(('>', name, '\n')))
        output.write(''.join(seq))
        output.write('\n')

    if close_output:
        output.close()
    else:
        output.flush()


def parse_aln(inputfile, outputfile):
    # This is as parse_fasta, but without printing the headers in the output.
    input_, close_input, output, close_output = _validate_input(inputfile, outputfile)

    data = defaultdict(list)
    reference_seq = []

    for line in input_:
        line = line.strip()
        if line and not line.startswith('#'):
            header, sequence = line.split()
            break

    while True:
        reference_seq.extend((s for s in sequence if s != '-'))
        index = [True if s != '-' else False for s in sequence]
        for line in input_:
            line = line.strip()
            if not line:
                break
            if not line.startswith('#'):
                try:
                    name, seq = line.split()
                    data[name].extend(s for s, i in zip(seq, index) if i)
                except ValueError:
                    # End of file
                    pass

        try:
            header, sequence = input_.next().split()
        except StopIteration:
            break

    if close_input:
        input_.close()
    os.system('vmtouch -qe {} & >/dev/null 2>/dev/null'.format(inputfile))

    # Write to file
    output.write(''.join(reference_seq))
    output.write('\n')

    for name, seq in data.iteritems():
        output.write(''.join(seq))
        output.write('\n')

    if close_output:
        output.close()
    else:
        output.flush()
