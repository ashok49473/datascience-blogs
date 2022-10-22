from haystack.nodes import TextConverter
from haystack.nodes import PreProcessor
from haystack.document_stores import SQLDocumentStore

# File converter 
converter = TextConverter(remove_numeric_tables=True, valid_languages=["en"])

# document store to save our text files 
# to see all available document stores, 
# visit: https://haystack.deepset.ai/components/document-store
document_store = SQLDocumentStore(url="sqlite:///qa.db")

# Preprocessor for text cleaning
preprocessor = PreProcessor(clean_empty_lines=True,
                            clean_whitespace=True,
                            clean_header_footer=False,
                            split_by="word",
                            split_length=100,
                            split_respect_sentence_boundary=True
                           )


doc_txt = converter.convert(file_path="document.txt", meta=None)[0] # converting text document
docs = preprocessor.process([doc_txt]) # preprocessing and splitting of document
document_store.write_documents(docs) # Indexing of docs to SQL document store

