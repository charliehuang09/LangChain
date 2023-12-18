import glob

from llama_index import Document
class Loader:
    def __init__(self, glob_path):
        self.files = glob.glob(glob_path)
    def load(self):
        docs = []
        for path in self.files:
            if path.endswith('.md'):
                docs.append(self.read_md(path))
    def read_md(path):
        text = open(path, "r").readlines()
        metadata = {
            "type" : "markdown",
            "path" : path
        }
        doc =  Document(page_content=text, metadata=metadata)
        return doc
    

    