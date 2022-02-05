from django.http import HttpResponse
from django.shortcuts import render
from hassanApp.models import Person
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


def index(request):
    context = {}

    personen_die_ich_auflisten_will = Person.objects.all()
    namen_der_spalten = Person._meta.get_fields()

    context["personen_die_ich_auflisten_will"] = personen_die_ich_auflisten_will
    context["namen_der_spalten"] = namen_der_spalten

    return render(request, "hassanApp/list.html", context)


def search(request):
    id_to_seach = request.GET.get("id")
    name_to_seach = request.GET.get("name")
    print(f"\n\nid_to_seach: {id_to_seach} name_to_seach: {name_to_seach}")

    if (not id_to_seach and not name_to_seach) == True:
        personsdic = Person.objects.all()

    else:
        if not id_to_seach:
            id_to_seach = 0

        if not name_to_seach:
            name_to_seach = ""

        personsdic = Person.objects.filter(pk=id_to_seach) | Person.objects.filter(
            first_name=name_to_seach
        )
        personsdic = Person.objects.filter(pk=id_to_seach).filter(
            first_name=name_to_seach
        )
    columnsdic = Person._meta.get_fields()
    context = {}

    context["personen_die_ich_auflisten_will"] = personsdic
    context["namen_der_spalten"] = columnsdic

    return render(request, "hassanApp/list.html", context)


class HassanAppUpdateView(UpdateView):
    # specify the model you want to use
    model = Person

    # specify the fields
    fields = ["first_name", "last_name"]

    # can specify success url
    # url to redirect after successfully
    # updating details

    def get_success_url(self):
        view_name = "index"
        return reverse_lazy(view_name)


def filter(data_to_filter) -> dict:
    return null
