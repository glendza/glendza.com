from wagtail import hooks


@hooks.register("register_icons")
def register_icons(icons):
    # TODO: Add / remove icons here
    # icons.remove("wagtailadmin/icons/time.svg")  # Remove the original icon
    # icons.append("path/to/time.svg")  # Add the new icon
    return icons
