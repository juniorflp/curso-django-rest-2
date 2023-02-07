from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {'email': {'write_only': True}}
        model = Avaliacao
        fields = ('id', 'curso', 'nome', 'email', 'comentario',
                  'avaliacao', 'criacao', 'ativo')


class CursoSerializer(serializers.ModelSerializer):
    # mostra somente no get as avaliacoes daquele curso (nested relationship) - ideal para poucos dados
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # gera um link para cada avaliacao na response (hyperlink related field)
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='avaliacao-detail')

    # mostra o id de todas avaliacoes (primary key related field) ideal para muitos dados.
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'ativo', 'avaliacoes')
