from django import template
from django.template.context import RequestContext

from glendza.web_app.apps.core.models import Menu

register = template.Library()


@register.simple_tag()
def get_menu(slug: str) -> Menu:
    return Menu.objects.get(slug=slug)


@register.inclusion_tag(
    name="navmenu",
    filename="core/snippets/navmenu.html",
    takes_context=True,
)
def render_navmenu(context: RequestContext, slug: str):
    try:
        menu = Menu.objects.prefetch_related("menu_items").get(slug=slug)
    except Menu.DoesNotExist:
        return {"menu_items": []}

    active_page = context["request"].path

    return {
        "menu_items": menu.menu_items.all(),
        "active_page": active_page,
    }
