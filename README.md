# pytemplate
A templating system for MS word.
The data must be in a CSV file. The template document must be a docx file.

# Notes on performance
With the test data (data.csv) and test template (template.docx), the `main.py` script managed to generate 1000 documents in 0.9116356s.
With the same data and template, the `threaded_main.py` script managed to generate 1000 documents in 5.3929732s.

The main.py script uses asyncio and concurrent.Futures.ThreadPoolExecutor to render and save the documents concurrently. The threaded_main.py script uses threading.

Although I am not exactly sure why this performance difference exists, I believe that it is because creating a Thread for every document in 1k documents is not a very good idea. For future renditions, I will be using a Queue. As for now, the async script provides over-average performance and exceeds my expectations, so I will not be changing it further.

# Usage:
Command Line utility:
```
py main.py <csv file path> <template document> <output folder>
```
# Dependancies
Python 3.8+

docxtpl module




