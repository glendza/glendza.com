from django.core.paginator import Paginator
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, ObjectList, TabbedInterface
from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail.models import Page

from glendza.web_app.types import GenericQuerySet

from .blog_page import BlogPage


class BlogIndexPage(RoutablePageMixin, Page):
    template = "core/blog/blog_index_page.html"
    max_count = 1
    pagination_page_param = models.CharField(
        default="page",
        help_text="Specify the query parameter to use for pagination.",
        max_length=255,
    )
    blog_posts_per_page = models.IntegerField(
        default=10,
        help_text="Specify the number of blog posts to display per page on the blog index.",
    )

    intro_text = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("intro_text"),
    ]

    settings_panels = Page.settings_panels + [
        MultiFieldPanel(
            [
                FieldPanel("pagination_page_param"),
                FieldPanel("blog_posts_per_page"),
            ],
            heading="Blog Index Page Settings",
        )
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(Page.promote_panels, heading="Promote"),
            ObjectList(settings_panels, heading="Settings"),
        ]
    )

    subpage_types = ["core.BlogPage"]

    def get_all_blog_posts(self) -> GenericQuerySet:
        return BlogPage.objects.live().descendant_of(self).order_by("-first_published_at")

    def get_blog_posts(self, request) -> GenericQuerySet:
        page = request.GET.get("page", 1)
        paginator = Paginator(self.get_all_blog_posts(), self.blog_posts_per_page)
        blog_posts = paginator.get_page(page)
        return blog_posts

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context.update(
            {
                "all_blog_posts": self.get_all_blog_posts(),
                "blog_posts": self.get_blog_posts(request),
                "blog_posts_per_page": self.blog_posts_per_page,
            },
        )
        return context
