from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet


class MenuItem(Orderable):
    link_title = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    link_url = models.CharField(
        max_length=500,
        null=True,
        blank=True,
    )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="menu_items",
    )
    open_in_new_tab = models.BooleanField(
        default=False,
        blank=True,
    )

    page = ParentalKey("core.Menu", related_name="menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    @property
    def link(self) -> str:
        if self.link_page:
            return self.link_page.url
        return self.link_url or "#"

    @property
    def title(self) -> str:
        if self.link_title:
            return self.link_title
        if self.link_page:
            return self.link_page.title
        return "Missing title"


@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=25,
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("title"),
                FieldPanel("slug"),
            ],
            heading="Menu",
        ),
        InlinePanel("menu_items", label="Menu Item"),
    ]

    def __str__(self) -> str:
        return self.title
