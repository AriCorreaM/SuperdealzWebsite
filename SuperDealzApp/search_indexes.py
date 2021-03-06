from haystack import indexes
from .models import Producto


class ProductoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # descripcion = indexes.CharField(model_attr='descripcion')
    # precio = indexes.CharField(model_attr='price')

    def get_model(self):
        return Producto

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
