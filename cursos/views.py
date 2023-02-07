from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import AvaliacaoSerializer, CursoSerializer


class CursoViewsSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # action serve para tornar avaliacoes uma rota dentro do curso
    # nao usa paginação global pq é uma classe customizada
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 2
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        # se tiver paginação
        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # se nao tiver paginação devolve todas avaliacoes deste curso.
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


class AvaliacaoViewsSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
