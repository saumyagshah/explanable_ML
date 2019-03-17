from django import forms
from .models import Document, Feature, ClassName, Parameter

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'document', )

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('feature',)

class ClassNameForm(forms.ModelForm):
    class Meta:
        model = ClassName
        fields = ('class_name',)

class ParameterForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = ('explainer', 'classifier', 'number_of_top_features', 'example_number_explain')