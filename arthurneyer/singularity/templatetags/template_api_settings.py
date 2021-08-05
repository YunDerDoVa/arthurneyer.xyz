from django import template

import singularity


register = template.Library()

@register.simple_tag
def FONT_AWESOME_TOKEN():
    return singularity.FONT_AWESOME_TOKEN
