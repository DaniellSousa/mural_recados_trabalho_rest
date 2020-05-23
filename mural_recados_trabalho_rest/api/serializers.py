from rest_framework.serializers import ModelSerializer
from mural_recados_trabalho_rest.models import Recado


class RecadoSerializer(ModelSerializer):
    class Meta:
        model = Recado
        fields = ["id", "texto", "apelido_usuario"]
