from rest_framework import serializers
from django.db.models import Avg  # classe para calcular media

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {'email': {'write_only': True}}
        model = Avaliacao
        fields = ('id', 'curso', 'nome', 'email', 'comentario',
                  'avaliacao', 'criacao', 'ativo')

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError(
            'A avaliacao precisa ser um numero inteiro entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    # mostra somente no get as avaliacoes daquele curso (nested relationship) - ideal para poucos dados
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # gera um link para cada avaliacao na response (hyperlink related field)
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='avaliacao-detail')

    # mostra o id de todas avaliacoes (primary key related field) ideal para muitos dados.
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # significa q o valor dele vai ser gerado por um metodo(função)
    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao',
                  'ativo', 'avaliacoes', 'media_avaliacoes')

    # a função tem que ter o nome com get na frente
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(
            Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2
