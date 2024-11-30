from langchain_community.document_loaders import PyPDFLoader
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

loader = PyPDFLoader("../../../documents/phaedo.pdf")
docs = loader.load()
documents = [{
        "content": docs[0],
        "book_name": "phaedo.pdf"
},
        {"content": docs[1],
        "book_name": "phaedo.pdf"
}]

client = QdrantClient(url="http://localhost:6333")
encoder = SentenceTransformer("all-MiniLM-L6-v2")

client.create_collection(
        collection_name="rag_collection",
        vectors_config=models.VectorParams(
            size=encoder.get_sentence_embedding_dimension(),
            distance=models.Distance.COSINE,
        ),
)

client.upload_points(
        collection_name="rag_collection",
        points=[
            models.PointStruct(
                id=idx, vector=encoder.encode(doc["content"]).toList(), payload=doc
        )
        for idx, doc in enumerate(documents)
        ],
)

print(docs[0], len(docs))

