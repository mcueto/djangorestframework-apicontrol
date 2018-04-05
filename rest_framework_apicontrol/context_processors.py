"""rest_framework_apicontrol context processors."""


def available_apps(request):
    """Return the available apps for the current user."""
    available_apps = None

    if request.user.is_authenticated:
        available_apps = request.user.app_set.all()

    return {
        'AVAILABLE_APPS': available_apps,
    }
