from django import template
from django.core.paginator import Paginator
from django.template.context import RequestContext

from glendza.web_app.types import GenericQuerySet

register = template.Library()


@register.inclusion_tag(
    "core/common/pagination.html",
    takes_context=True,
)
def paginate(context: RequestContext, queryset: GenericQuerySet, *, per_page=10, page_var="page"):
    request = context["request"]
    page_number = request.GET.get(page_var, 1)

    paginator = Paginator(queryset, per_page)
    page_obj = paginator.get_page(page_number)

    return {
        "page_obj": page_obj,
        "paginator": paginator,
        "request": request,
        "page_var": page_var,
    }
