from django import template

register = template.Library()


@register.filter
def cycle_icons(icons, counter):
    return icons[counter % len(icons)]
