from .reader import Reader
from docxtpl import DocxTemplate
from concurrent.futures import ThreadPoolExecutor

class Template(DocxTemplate):
    '''Standard template class for loading and rendering .docx files'''

    def __init__(self, fp: str, out: str):
        super().__init__(fp)
        self.out = out

    def render(self, reader: Reader):
        with ThreadPoolExecutor() as executor:
            for i, row in enumerate(reader.data):
                executor.submit(self.save, f"{self.out}/{i}.docx", dict(zip(reader.fields, row)))

    def save(self, path, context):
        print(path)
        super().render(context)
        super().save(path)