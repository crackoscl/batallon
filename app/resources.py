from import_export import resources
from .models import Rating
class RatingResource(resources.ModelResource):
    class Meta:
        model = Rating
        fields = (
            'id',
            'rank',
            'categoria',
            'peleador',
            'rating',
            'rd',
            'peleador__nombre'

        )