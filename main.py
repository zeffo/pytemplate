
""" 
MS Word Automated Templating
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Templating system in Python3 for Microsoft Word

For information on usage, check the readme (README.md)
To report bugs or give feedback, please write to le32@myshala.com
All feedback is appreciated.

"""

import csv
from docxtpl import DocxTemplate
from sys import argv
import threading
from time import perf_counter


class Reader(object):
    ''' Class to help parse the CSV data. '''
    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.f = open(self.target)
        self.reader = csv.reader(self.f)
        self.data = [row for row in self.reader]
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.f.close()

    @property
    def fields(self):
        return self.data[0]

def transform(doc, context, output, index):
    ''' Renders and saves the document. '''
    doc.render(context)
    doc.save(f'{output}/{index}.docx')
        

def main() -> None:
    ''' Main function that handles and coordinated all other helper functions. '''
    _data, template, output = argv[1:]
        
    with Reader(_data) as reader:
        fields = reader.fields
        data = reader.data[1:]
    for index, row in enumerate(data):
        context = dict(zip(fields, row))
        doc = DocxTemplate(template)
        thread = threading.Thread(target=transform, args=(doc, context, output, index))
        thread.start()
    

if __name__ == '__main__':
    start = perf_counter()
    main()
    end = perf_counter()
    print(f'Finished with {round(end-start, 2)}s')









































