import streamlit as st

from haystack.document_stores import SQLDocumentStore
from haystack.nodes import FARMReader, TfidfRetriever
from haystack.pipelines import ExtractiveQAPipeline

reader = FARMReader(model_name_or_path="reader") # loading the saved reader model

document_store = SQLDocumentStore(url="sqlite:///qa.db") # SQL documentstore

retriever = TfidfRetriever(document_store=document_store) # initializing

pipe = ExtractiveQAPipeline(reader, retriever) # Prediction pipeline 


st.title("Question Answering system")
question = st.text_area("Enter your question:") # taking query
if st.button("Answer"):
    params={"Retriever": {"top_k": 5}, "Reader": {"top_k": 3}}
    prediction = pipe.run(query=question, params=params)
    
    # show results
    for ans in prediction['answers']:
        st.write(ans.answer) # main answer
        st.write(ans.context) # context
        st.write('---')


