from django.contrib import admin

from .models import Work
from .models import InstagramPortfolio, WorkPortfolio, MuggumPortfolio


# Register your models here.
admin.site.register(Work)
admin.site.register(InstagramPortfolio)
admin.site.register(WorkPortfolio)
admin.site.register(MuggumPortfolio)
