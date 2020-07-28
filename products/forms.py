from django import forms
from .models import Product, Category, Genre, ComingSoon


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        genres = Genre.objects.all()
        genre_friendly_names = [(g.id, g.get_friendly_name()) for g in genres]

        self.fields['category'].choices = category_friendly_names
        self.fields['genre'].choices = genre_friendly_names


class ComingSoonForm(forms.ModelForm):

    class Meta:
        model = ComingSoon
        fields = '__all__'
