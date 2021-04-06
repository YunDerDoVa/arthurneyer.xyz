from django.db import models

# Create your models here.
class Work(models.Model):

    title = models.CharField(max_length=63)
    subtitle = models.CharField(max_length=63)


class Portfolio(models.Model):

    name = models.CharField(max_length=63)

    image = models.ImageField(upload_to="images/portfolio/")
    alt_image = models.TextField(max_length=255)

    link = models.URLField()
    label_link = models.CharField(max_length=63)

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=63)
    subtitle = models.CharField(max_length=63)

    description = models.TextField(max_length=255)

    class Meta:
        abstract = True

    def get_portfolio_type(self):
        return 'BASE'

class InstagramPortfolio(Portfolio):

    photo_id = models.CharField(max_length=63)

    def get_portfolio_type(self):
        return 'INSTA'

class WorkPortfolio(Portfolio):

    work = models.ForeignKey(Work, on_delete=models.SET_NULL, null=True)

    def get_portfolio_type(self):
        return 'WORK'

class MuggumPortfolio(Portfolio):

    work = models.ForeignKey(Work, on_delete=models.SET_NULL, null=True)

    def get_portfolio_type(self):
        return 'MUGGUM'
