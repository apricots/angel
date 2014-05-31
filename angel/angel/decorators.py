from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def basic_profile_and_match_info_required(view_func):
    """Redirects a user to the appropriate settings page if basic profile information is missing"""

    def _wrapped_view_func(request, *args, **kwargs):

        ### Has the user gone through the onboarding process
        if not request.user.onboarding_progress.complete():
            return HttpResponseRedirect(reverse('onboarding'))

        ### Has the user filled out all basic match information

        return view_func(request, *args, **kwargs)

    return _wrapped_view_func