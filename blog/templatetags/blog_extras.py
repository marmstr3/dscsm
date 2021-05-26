from django import template

# Custom Filters
register = template.Library()

@register.filter(name='get_range1')
def get_range1(range_size=1):
    return range(1, range_size+1)


@register.filter(name='get_range0')
def get_range0(range_size=1):
    return range(range_size)