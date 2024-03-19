""""
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize

# Sample documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# Tokenize using NLTK's word_tokenize
tokenized_documents = [word_tokenize(doc) for doc in documents]

# CountVectorizer (Bag of Words)
count_vectorizer = CountVectorizer()
X_count = count_vectorizer.fit_transform([' '.join(tokens) for tokens in tokenized_documents])

# TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform([' '.join(tokens) for tokens in tokenized_documents])

print(f"tokenized document: {tokenized_documents}")

# To see the vocabulary (unique words)
print("Vocabulary for CountVectorizer:")
print(count_vectorizer.get_feature_names_out())

print("\nVocabulary for TF-IDF Vectorizer:")
print(tfidf_vectorizer.get_feature_names_out())

# To see the vectorized representation of documents
print("\nVectorized representation for CountVectorizer:")
print(X_count.toarray())

print("\nVectorized representation for TF-IDF Vectorizer:")
print(X_tfidf.toarray())
"""



#SecondBrainVector@gmail.com
#SecondBrainVector1!

#https://www.pinecone.io/


import pinecone
import pandas as pd

pinecone.init(api_key="d489c9e2-5765-423f-ab5a-5da2eabb2d14", environment="gcp-starter")
index = pinecone.Index("test")



#https://docs.google.com/document/d/1cS1TBS-nr5zXRfmm3Li3qMA4v6VUxegEmHpRXg7Ru00/edit?usp=sharing

from langchain.document_loaders import PyPDFLoader
from sentence_transformers import SentenceTransformer

# Load PDF and extract text
loader = PyPDFLoader("example4.pdf")
pages = loader.load_and_split()

# Extracted text from the PDF joined into single string
document_text = ''.join([page.page_content for page in pages])

# Use Sentence Transformers to generate an embedding for the entire document
model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')
document_embedding = model.encode([document_text])

# 'document_embedding' now contains the vector representation of the entire document
print(document_embedding)


flat = document_embedding.tolist()
print(flat)

df = pd.DataFrame(
    data={
        "id": ["FirstDoc"],
        "vector": flat
    })
df

index.upsert(vectors=(zip(df.id, df.vector)))  # insert new vectors or update the vector if the id was already created



""""
print(index.query(
    vector=[3., 5., 5.],
    top_k=2,
    include_values=True)) # returns top_k matches

"""