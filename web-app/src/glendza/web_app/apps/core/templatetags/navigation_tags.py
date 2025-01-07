from django import template
from django.template.context import RequestContext
from wagtail.models import Site

register = template.Library()


@register.simple_tag(name="site_root", takes_context=True)
def get_site_root(context: RequestContext):
    return Site.find_for_request(context["request"]).root_page
