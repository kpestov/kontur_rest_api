import django.urls
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode


def reverse(view, urlconf=None, args=None, kwargs=None, current_app=None, query_kwargs=None):
    base_url = django.urls.reverse(view, urlconf=urlconf, args=args, kwargs=kwargs, current_app=current_app)

    if query_kwargs:
        return f'{base_url}?{urlencode(query_kwargs, doseq=isinstance(query_kwargs, MultiValueDict))}'

    return base_url
