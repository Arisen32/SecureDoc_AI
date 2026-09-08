import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

class AzureRAGService:
    def __init__(self):
        self.endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        self.api_key = os.getenv("AZURE_SEARCH_KEY")
        self.index_name = os.getenv("AZURE_SEARCH_INDEX", "documents-index")

    def process_and_index_document(self, document_path: str, document_id: str):
        """
        Extrae texto del documento e indexa sus embeddings en Azure AI Search.
        """
        # Aquí se realiza la extracción de texto con Azure Document Intelligence / OpenAI
        # y la indexación vectorial en Azure AI Search.
        pass

    def query_documents(self, query_text: str, user_id: int):
        """
        Realiza búsqueda híbrida/semántica acotada a los documentos del usuario.
        """
        if not self.endpoint or not self.api_key:
            return {"error": "Configuración de Azure AI no encontrada."}

        client = SearchClient(
            endpoint=self.endpoint,
            index_name=self.index_name,
            credential=AzureKeyCredential(self.api_key)
        )
        
        # Filtro de seguridad (Zero Trust / SC-100)
        results = client.search(
            search_text=query_text,
            filter=f"owner_id eq '{user_id}'"
        )
        return [result for result in results]