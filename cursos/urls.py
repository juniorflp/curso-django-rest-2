from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import CursoViewsSet, AvaliacaoViewsSet


router = SimpleRouter()
router.register('cursos', CursoViewsSet)
router.register('avaliacoes', AvaliacaoViewsSet)
