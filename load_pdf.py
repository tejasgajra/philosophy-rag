from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./documents/phaedo.pdf")
docs = loader.load()

print(docs[0], len(docs))
