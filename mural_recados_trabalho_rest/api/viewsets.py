from rest_framework.viewsets import ModelViewSet
from mural_recados_trabalho_rest.api.serializers import RecadoSerializer
from mural_recados_trabalho_rest.models import Recado


class RecadoViewSet(ModelViewSet):
    serializer_class = RecadoSerializer
    queryset = Recado.objects.all()
