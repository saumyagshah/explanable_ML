from django.db import models

class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'document uploaded at ' + str(self.uploaded_at)  

class Feature(models.Model):
    feature = models.CharField(max_length=2000)
    def __str__(self):
        return self.feature

class ClassName(models.Model):
    class_name = models.CharField(max_length=2000)
    def __str__(self):
        return self.class_name

EXPLAINER_CHOICES = (('LIME', 'LIME'), ('A-LIME', 'A-LIME'),)

CLASSIFIER_CHOICES = (('Nearest Neighbour', 'Nearest Neighbour'),
                    ('Linear SVM', 'Linear SVM'),
                    ('RBF SVM', 'RBF SVM'),
                    ('Gaussian Process', 'Gaussian Process'),
                    ('Decision Tree', 'Decision Tree'),
                    ('Random Forest', 'Random Forest'),
                    ('Neural Net', 'Neural Net'),
                    ('Naive Bayes', 'Naive Bayes'),
                    ('AdaBoost', 'AdaBoost'),('QDA', 'QDA'))

class Parameter(models.Model):
    explainer = models.CharField(max_length=10, choices=EXPLAINER_CHOICES)
    classifier = models.CharField(max_length=50, choices=CLASSIFIER_CHOICES)
    number_of_top_features = models.IntegerField()
    example_number_explain = models.IntegerField()

    def __str__(self):
        return str(self.explainer) + ' ' + str(self.classifier) + ' ' + str(self.number_of_top_features) + ' ' + str(self.example_number_explain)

