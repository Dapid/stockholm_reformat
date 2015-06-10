====
 stockholm_reformat
====

Fast Stockholm to A3M Multiple Sequence Alignment reformater

Includes an API and a command line script. The pure Python version is already several times faster than the
Perl script contained in the `MPI Bioinformatics Toolkit. <http://toolkit.tuebingen.mpg.de/reformat/help_params>`


Usage
----
From Python::

    stockholm_reformat.parse('inputfile', 'outputfile')

From the command line::

    $ stockholm_to_a3m input.sto output.a3m
