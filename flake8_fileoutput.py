__version__ = '0.1'

import pep8


class FileOutputReport(pep8.BaseReport):
    '''Collect and print the results of the checks.'''

    def __init__(self, options):
        super(FileOutputReport, self).__init__(options)
        self._outputfile = options.fileoutput

    def error(self, line_number, offset, text, check):
        '''Report an error, according to options.'''
        code = super(FileOutputReport, self).error(line_number, offset, text, check)
        with open(self._outputfile, 'w') as f:
            f.write(code)
        return code


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
