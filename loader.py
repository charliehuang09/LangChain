import glob
from langchain.docstore.document import Document
class Loader:
    def __init__(self, glob_path):
        self.files = glob.glob(glob_path, recursive=True)
    def load(self):
        docs = []
        for path in self.files:
            if path.endswith('.md'):
                docs.append(self.read_md(path))
            if path.endswith('.sh'):
                docs.append(self.read_sh(path))
        return docs
    def read_md(self, path):
        text = open(path, "r").readlines()
        text = "".join(text)
        metadata = {
            "type" : "markdown",
            "path" : path
        }
        doc =  Document(page_content=text, metadata=metadata)
        return doc
    
    def read_sh(self, path):
        text = open(path, "r").readlines()
        text = "".join(text)
        metadata = {
            "type" : "shell",
            "path" : path
        }
        doc =  Document(page_content=text, metadata=metadata)
        return doc
    

    