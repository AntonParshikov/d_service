from django import template

register = template.Library()


@register.filter()
def distribution_media(val):
    if val:
        return f'/media/{val}'

    return '/media/distribution/Рассылка.jpg'
