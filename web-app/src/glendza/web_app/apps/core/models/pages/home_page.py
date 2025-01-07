from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from glendza.web_app.apps.core import blocks as core_blocks


class HomePage(Page):
    template = "core/home_page.html"
    max_count = 1

    content = StreamField(
        block_types=[
            (
                "hero_section",
                core_blocks.HeroSectionBlock(),
            )
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "home page"
        verbose_name_plural = "home pages"
