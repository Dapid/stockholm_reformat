import os
from collections import defaultdict


def cparse(inputfile, outputfile):
    # Pre-load the file in memory, if vmtouch is installed.
    os.system('vmtouch -qt {} & >/dev/null 2>/dev/null'.format(inputfile))
    cdef str line, header, sequence, name, seq
    cdef str s
    cdef short int i
    cdef list data_name

    input_ = open(inputfile)
    output = open(outputfile, 'w')

    data = defaultdict(list)
    reference_seq = []

    for line in input_:
        line = line.strip()
        if line and not line.startswith('#'):
            header, sequence = line.split()
            break

    while True:
        reference_seq.extend((s for s in sequence if s != '-'))
        index = [1 if s != '-' else 0 for s in sequence]
        for line in input_:
            line = line.strip()
            if not line:
                break
            if not line.startswith('#'):
                try:
                    name, seq = line.split()
                    data_name = data[name]
                    for s, i in zip(seq, index):
                        if i or s != '-':
                            if not i:
                                s = s.lower()
                            data_name.append(s)
                except ValueError:
                    # End of file
                    pass

        try:
            header, sequence = input_.next().split()
        except StopIteration:
            break

    input_.close()
    os.system('vmtouch -qe {} & >/dev/null 2>/dev/null'.format(inputfile))

    # Write to file
    output.write(''.join(('>', header, '\n')))
    output.write(''.join(reference_seq))
    output.write('\n')

    for name, seq_l in data.iteritems():
        output.write(''.join(('>', name, '\n')))
        output.write(''.join(seq_l))
        output.write('\n')
    output.close()