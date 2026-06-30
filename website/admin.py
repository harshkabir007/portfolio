from website.models import Achievement
from website.models import Skill
from website.models import Project
from website.models import Contact
from website.models import Gallery
from website.models import Certificate
from website.models import Experience
from django.contrib import admin

from .models import *

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Achievement)
admin.site.register(Experience)
admin.site.register(Certificate)
admin.site.register(Gallery)
admin.site.register(Contact)