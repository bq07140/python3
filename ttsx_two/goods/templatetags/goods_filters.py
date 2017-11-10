from django.template import Library

register = Library()


@register.filter
def cag_image(index):

    return 'images/banner0' + str(index) + '.jpg'

