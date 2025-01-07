from django import template
from django.template.context import RequestContext

from glendza.web_app.apps.core.models import FooterContent, HeaderContent

register = template.Library()


@register.inclusion_tag(
    "core/snippets/header.html",
    takes_context=True,
)
def header(context: RequestContext):
    base_context: dict = {
        "page": context.get("page"),
        "request": context.get("request"),
    }

    header_content = context.get("header_data", "")

    if not header_content:
        header_content = HeaderContent.objects.filter(live=True).first()

    if not header_content:
        return base_context

    return base_context | {
        "logo": header_content.logo,
    }


@register.inclusion_tag(
    "core/snippets/footer.html",
    takes_context=True,
)
def footer(context: RequestContext):
    base_context: dict = {}
    footer_content = context.get("footer_data", "")

    if not footer_content:
        footer_content = FooterContent.objects.filter(live=True).first()

    if not footer_content:
        return base_context

    return base_context | {
        "copyright_text": footer_content.copyright_text,
        "github_url": footer_content.github_url,
    }
