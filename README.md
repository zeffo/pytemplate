# pytemplate
A templating system for MS word.
The data must be in a CSV file. The template document must be a docx file.

# Notes on performance
With the test data (data.csv) and test template (template.docx), the `main.py` script managed to generate 1000 documents in 0.9116356s.
With the same data and template, the `threaded_main.py` script managed to generate 1000 documents in 5.3929732s.

The main.py script uses asyncio and concurrent.Futures.ThreadPoolExecutor to render and save the documents concurrently. The threaded_main.py script uses threading.

(The performance difference exists due to the GIL.)

# Usage:
Command Line utility:
```
py main.py <csv file path> <template document> <output folder>
```
# Dependancies
Python 3.8+

docxtpl module (You can install this from PyPI: https://pypi.org/project/docxtpl/)




