from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Outfit


def create(request, template):
    """Creates or returns form to create an outfit"""

    if request.method == 'POST':

        if 'message' in request.POST and 'picture' in request.FILES:
            outfit = Outfit(
                user=request.user,
                picture=request.FILES['picture'],
                message=request.POST['message']
            )

            outfit.save()
            return HttpResponseRedirect(reverse('view-outfit-rating', args=(outfit.pk,)))

        return render(request, template)
    else:
        return render(request, template)


def view_rating(request, template, outfit_id):
    """Where a user can watch real time ratings of their outfits"""
    context = {
        'outfit': Outfit.objects.get(id=outfit_id)
    }
    return render(request, template, context)
