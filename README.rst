====
 stockholm_reformat
====

Fast Stockholm Multiple Sequence Alignment reformater.

Includes an API and a command line script. The pure Python version is already several times faster than the
Perl script contained in the `MPI Bioinformatics Toolkit. <http://toolkit.tuebingen.mpg.de/reformat/help_param>`_

The following outuput supported formats are:

 * a3m
 * fasta
 * aln

Usage
----
From Python::

    stockholm_reformat.parse_a3m('inputfile.sto', 'outputfile.a3m')
    stockholm_reformat.parse_fasta('inputfile.sto', 'outputfile.fasta')
    stockholm_reformat.parse_aln('inputfile.sto', 'outputfile.aln')

If you have a working C compiler, you may have the compiled versions installed::

    stockholm_reformat.cparse_a3m('inputfile.sto', 'outputfile.a3m')
    stockholm_reformat.cparse_fasta('inputfile.sto', 'outputfile.fasta')
    stockholm_reformat.cparse_aln('inputfile.sto', 'outputfile.aln')

They are around twice as fast, but the input must be the file name, not a file handler (easily fixable, if needed).

From the command line::

    $ stockholm_to_a3m input.sto output.a3m
    $ stockholm_to_fasta input.sto output.fasta
    $ stockholm_to_aln input.sto output.aln
