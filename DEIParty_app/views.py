from django.shortcuts import render
from django.http import HttpResponse

from DEIParty_app.retrieve_functions import list_all_beverages, get_beverage_info, process_removal, process_update

# request handlers in a nuthsell


def request_handler_teste(request):
    return HttpResponse("Isto é um teste")


def request_handler_2o_teste(request):
    return HttpResponse("Isto é outro teste")


def html_bonito(request):
    return render(request, "boas.html", {"nome": "Chaps"})


def process_error(request):
    return render(request, "error_page.html")


def show_all_beverages(request, limit, offset):
    # each beverage has the following info: "id", "designation","amountInStock", "imageUrl", "supplier"

    beverages = list_all_beverages(limit, offset)
    params = {"beverages": beverages}

    return render(request, "list_all_beverages.html", params)


def show_beverage(request, id):

    beverage = get_beverage_info(id)
    params = {"beverage": beverage}

    return render(request, "list_beverage.html", params)


def warn_user(request, id):
    beverage = get_beverage_info(id)
    params = {"beverage": beverage}
    return render(request, "warn_user.html", params)


def confirm_removal(request, id):

    res = process_removal(id)

    if res == 400:
        return HttpResponse("O ID da bebida é inválido")
    elif res == 401:
        return HttpResponse("O Token de Acesso está em falta ou é inválido")
    elif res == 403:
        return HttpResponse("Não tem permissão para realizar a operação")
    elif res == 404:
        return HttpResponse("A bebida não foi encontrada")

    return render(request, "removal_success.html")


def update_beverage(request, id, new_quantity):

    res = process_update(id, new_quantity)

    if res == 200:
        return HttpResponse("SUCESSO!!!")
    elif res == 400:
        return HttpResponse("A bebida é inválida")
    elif res == 404:
        return HttpResponse("A bebida não foi encontrada")
    elif res == 409:
        return HttpResponse("A designação da bebida não pode ser alterada")
