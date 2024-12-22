from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Announcement
from main.models import Store
from django.utils.html import strip_tags
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .forms import AnnouncementForm
from django.urls import reverse
import json
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
@require_POST
def create_announcement_ajax(request):
    title = strip_tags(request.POST.get("title"))
    description = strip_tags(request.POST.get("description"))
    store_id = request.POST.get("store_id")

    user = request.user.ajeg_user
    store = Store.objects.get(pk=store_id)
    if store not in user.merchant_store:
        return HttpResponse(b"UNAUTHORIZED", status=403)

    announcement = Announcement(title=title, description=description, store_id=store_id)
    announcement.save()

    return HttpResponse(b"CREATED", status=201)


def get_announcements_by_store(request, store_id):
    data = Announcement.objects.filter(store_id=store_id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def get_announcement_by_id(request, id):
    data = Announcement.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def edit_announcement(request, id):
    announcement = Announcement.objects.get(pk=id)
    form = AnnouncementForm(request.POST or None, instance=announcement)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(
            reverse("checkout:store_page", args=[announcement.store.id])
        )

    context = {"form": form}
    return render(request, "edit_announcement.html", context)


def delete_announcement(request, id):
    announcement = Announcement.objects.get(pk=id)

    user = request.user.ajeg_user
    if announcement.store not in user.merchant_store:
        return HttpResponse(b"UNAUTHORIZED", status=403)

    announcement.delete()
    return HttpResponseRedirect(
        reverse("checkout:store_page", args=[announcement.store.id])
    )

@csrf_exempt
def create_announcement_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_announcement = Announcement.objects.create(
            title=data["title"],
            description=data["description"],
            store_id=int(data["store"]),
        )

        new_announcement.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def edit_announcement_flutter(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        try:
            announcement = Announcement.objects.get(pk=id)
        except Announcement.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Announcement not found"}, status=404)

        announcement.title = data["title"]
        announcement.description = data["description"]
        announcement.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def delete_announcement_flutter(request, id):
    announcement = Announcement.objects.get(pk=id)
    announcement.delete()
    return JsonResponse({"status": "success"}, status=200)

def get_all_announcements(request):
    data = Announcement.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )
