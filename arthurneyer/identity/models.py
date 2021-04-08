from django.db import models

# Create your models here.
class Work(models.Model):

    title = models.CharField(max_length=63)
    subtitle = models.CharField(max_length=63)


class Portfolio(models.Model):

    name = models.CharField(max_length=63)
    homepage = models.CharField(max_length=7, null=True, blank=True)

    image = models.ImageField(upload_to="images/portfolio/")
    alt_image = models.TextField(max_length=255)

    link = models.URLField()
    label_link = models.CharField(max_length=63)

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=63, null=True, blank=True)
    subtitle = models.CharField(max_length=63, null=True, blank=True)

    description = models.TextField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return float(self.homepage) < float(other.homepage)

    def get_portfolio_type(self):
        return 'BASE'

    @staticmethod
    def get_all_portfolios():

        portfolios = []
        portfolios_classnames = [
            'WorkPortfolio',
            'MuggumPortfolio',
            'InstagramPortfolio',
        ]

        for classname in portfolios_classnames:
            portfolio = eval(classname)
            for item in portfolio.objects.order_by('homepage').all():
                portfolios.append(item)

        return portfolios

class InstagramPortfolio(Portfolio):

    insta_id = models.CharField(max_length=63, null=True, blank=True)
    photo_id = models.CharField(max_length=63, null=True, blank=True)

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
