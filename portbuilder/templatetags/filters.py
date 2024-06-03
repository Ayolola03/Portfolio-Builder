from django import template

register = template.Library()


@register.filter(name="mastery_to_percentage")
def mastery_to_percentage(mastery_level):
    mapping = {
        "beginner": 25,
        "intermediate": 50,
        "advanced": 75,
        "expert": 100,
    }
    return mapping.get(mastery_level, 0)  # Default to 0 if mastery_level is not found
