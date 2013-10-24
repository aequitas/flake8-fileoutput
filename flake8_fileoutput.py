from __future__ import print_function
__version__ = '0.1'

import pep8


class FileOutputReport(pep8.StandardReport):
    '''Output results to file.'''

    def __init__(self, options):
        super(FileOutputReport, self).__init__(options)
        self._file = open(options.fileoutput, 'w')

    def get_file_results(self):
        """Write the result to file."""
        super(FileOutputReport, self).get_file_results()

        for line_number, offset, code, text, doc in self._deferred_print:
            print(self._fmt % {
                'path': self.filename,
                'row': self.line_offset + line_number, 'col': offset + 1,
                'code': code, 'text': text,
            }, file=self._file)
            if self._show_source:
                if line_number > len(self.lines):
                    line = ''
                else:
                    line = self.lines[line_number - 1]
                print(line.rstrip(), file=self._file)
                print(' ' * offset + '^', file=self._file)
            if self._show_pep8 and doc:
                print(doc.lstrip('\n').rstrip(), file=self._file)
        return self.file_errors


class FileOutput(object):

    name = 'flake8-fileoutput'
    version = __version__

    def __init__(self):
        pass

    @classmethod
    def add_options(cls, parser):
        parser.add_option('--fileoutput', type=str,
                          help='file to store the output to')

    @classmethod
    def parse_options(cls, options):
        if options.fileoutput:
            options.report = FileOutputReport(options)
