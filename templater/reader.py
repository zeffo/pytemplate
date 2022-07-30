import re
from docxtpl import DocxTemplate
from typing import Union
from io import TextIOWrapper


class Reader:
    '''Parser for CSV files'''

    def __init__(self, file: TextIOWrapper, delimiter=','):
        self.delimiter = delimiter
        self.file = file
        self.data = [row.split(delimiter) for row in file.read().split('\n')]
        self.fields = self.data.pop(0)

    def __len__(self):
        return len(self.data)
    



    



