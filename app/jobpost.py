import pandas as pd
import chromadb
import uuid


class Jobpost:
    def __init__(self, file_path="app/resource/roles_skills_links.csv"):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient("vectorstore")
        self.collection_names = self.chroma_client.list_collections()
        self.collection = self.chroma_client.get_or_create_collection(name="skills")

    def load_jobpost(self):
        if not self.collection.count():
            for _, row in self.df.iterrows():
                self.collection.add(
                    documents=row["Skills"],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())],
                )

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get("metadatas", [])
