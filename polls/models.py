from django.db import models
from view_table.models import ViewTable


class Book(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)


class Books(ViewTable):
    category = models.CharField(primary_key=True, unique=False, max_length=100)
    count = models.IntegerField()

    @classmethod
    def get_query(self):
        return Book.objects.values('category').annotate(count=models.Count('category')).query
