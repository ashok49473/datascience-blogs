from haystack.nodes import TfidfRetriever
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline

# https://haystack.deepset.ai/pipeline_nodes/retriever
retriever = TfidfRetriever(document_store=document_store)

# https://haystack.deepset.ai/pipeline_nodes/reader
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")
reader.save('reader') # saving reader model

sample_query = "Who inspired the author to write this book?"
params={"Retriever": {"top_k": 5}, # Top 5 relevant documents in document_store
        "Reader": {"top_k": 3} # Top 3 answers, searched in retrieved documents.
       } 
prediction = pipe.run(query=sample_query, params=params)

print(prediction['answers'])

# Output - top 3 relevant answers from documents
# [<Answer {'answer': 'Andrew Carnegie', 'type': 'extractive', 'score': 0.5995014905929565, 'context': ' goal. Somewhere in
# the book you will find this needed stimulus. The book was inspired by Andrew Carnegie, after he had made his
# millions and retired.', 'offsets_in_document': [{'start': 510, 'end': 525}], 'offsets_in_context': [{'start': 90, 'end': 105}], 'document_id': '5c872c45a63559566e566a02eccc81cc', 'meta': {'_split_id': '29'}}>,
 
 
#  <Answer {'answer': 'Patrick Henry', 'type': 'extractive', 'score': 0.5552873611450195, 'context': "Inspired by the threat, one of Jefferson's colleagues, Patrick Henry,
# boldly spoke his mind, concluding his remarks with a sentence which shall
# remain", 'offsets_in_document': [{'start': 55, 'end': 68}], 'offsets_in_context': [{'start': 55, 'end': 68}], 'document_id': '8e9e1ccf156987478e51a52f18e28539', 'meta': {'_split_id': '692'}}>,
 

#  <Answer {'answer': 'Andrew Carnegie', 'type': 'extractive', 'score': 0.10823056101799011, 'context': ' to aim high, and NOT
# MISTAKE TEMPORARY DEFEAT FOR FAILURE, just as Andrew Carnegie, the
# great industrial leader, inspired his young business lieutena', 'offsets_in_document': [{'start': 333, 'end': 348}], 'offsets_in_context': [{'start': 68, 'end': 83}], 'document_id': '1c04800567c27409fc5ef1f4d556f57a', 'meta': {'_split_id': '390'}}>]


