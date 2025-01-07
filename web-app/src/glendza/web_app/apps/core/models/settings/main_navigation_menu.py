from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class MainNavigationMenuSetting(BaseSiteSetting):
    menu = models.ForeignKey(
        "core.Menu",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="+",
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("menu"),
            ],
            heading="Main Navigation Menu",
        ),
    ]

    class Meta:
        verbose_name = "Main Navigation Menu"
