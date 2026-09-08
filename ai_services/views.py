from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .rag_engine import AzureRAGService

class DocumentQueryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        query_text = request.data.get('query')
        if not query_text:
            return Response(
                {"error": "El campo 'query' es obligatorio."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        rag_service = AzureRAGService()
        results = rag_service.query_documents(
            query_text=query_text, 
            user_id=request.user.id
        )

        return Response({
            "query": query_text,
            "results": results
        }, status=status.HTTP_200_OK)