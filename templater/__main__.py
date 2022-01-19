import argparse
import os
from .template import Template
from .reader import Reader
from time import perf_counter

parser = argparse.ArgumentParser(description="DocX Template renderer")


parser.add_argument('template')
parser.add_argument('data', type=argparse.FileType('r', encoding=None))
parser.add_argument('-out', default=os.getcwd()+'\\out')
parser.add_argument('-l', default='index', nargs='?')
parser.add_argument('-d', default=',', nargs='?')

parsed = parser.parse_args()

reader = Reader(parsed.data, delimiter=parsed.d)
template = Template(parsed.template, parsed.out)

start = perf_counter()
template.render(reader)
print("Finished in ", perf_counter()-start, "s")