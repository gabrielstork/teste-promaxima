from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from . import models
from . import forms
from . import helpers


def index(request):
    """
    Lista os dados de acordo com a preferência do usuário, e caso o usuário
    atualize esses mesmos dados, todos dados que foram coletados, ou seja, os
    que não foram criados manualmente, são excluídos e substituídos por novos
    atualizados.
    """
    previous_link = request.GET.get('previous_link', '/')

    if request.method == 'GET':
        order = request.GET.get('order', 'tipo')
        items_per_page = int(request.GET.get('items', '25'))

        items = models.GasolinaComum.objects.all().order_by(order)
        items_count = items.count()

        try:
            registro = models.Registro.objects.latest('id')
        except ObjectDoesNotExist:
            registro = 'Nenhuma'

        paginator = Paginator(items, items_per_page)
        page_number = request.GET.get('page', 1)

        try:
            page = paginator.page(page_number)
        except EmptyPage:
            page = paginator.page(1)

        context = {
            'page_range': paginator.page_range,
            'items': page,
            'items_count': items_count,
            'order_value': order,
            'order_value_text': helpers.ORDER_BY.get(order),
            'items_per_page_value': items_per_page,
            'page_value': int(page_number),
            'registro': registro,
            'previous_link_value': previous_link,
        }

        return render(request, 'gasolina_comum/index.html', context)

    elif request.method == 'POST':
        models.GasolinaComum.objects.filter(raspagem=True).delete()
        dados = helpers.obter_dados()

        for dado in dados:
            models.GasolinaComum.objects.create(
                tipo=dado.get('tipo'),
                valor_unitario=dado.get('valor_unitario'),
                valor_ultima_venda=dado.get('valor_ultima_venda'),
                tempo_ultima_venda=dado.get('tempo_ultima_venda'),
                contribuinte=dado.get('contribuinte'),
                codigo=dado.get('codigo'),
                raspagem=True,
            )

        models.Registro.objects.create()

        return redirect(previous_link)


def add(request):
    """
    Exibe um form que deve ser preenchido pelo usuário possibilitando a adição
    de um novo item no banco de dados.
    """
    previous_link = request.GET.get('previous_link', '/')

    if request.method == 'GET':
        add_form = forms.GasolinaComumForm()

        context = {
            'add_form': add_form,
            'previous_link_value': previous_link,
        }

        return render(request, 'gasolina_comum/add.html', context)
    elif request.method == 'POST':
        add_form = forms.GasolinaComumForm(request.POST)

        if add_form.is_valid():
            add_form.save()

        return redirect(previous_link)


def edit(request, pk):
    """
    Obtém o item no banco de dados, caso ele exista, e exibe as informações
    em um form para que o usuário possa as editar, salvar as alterações ou
    cancelar a operação, voltando à pagina anterior.
    """
    previous_link = request.GET.get('previous_link', '/')
    item = get_object_or_404(models.GasolinaComum, pk=pk)

    if request.method == 'GET':
        edit_form = forms.GasolinaComumForm(instance=item)

        context = {
            'edit_form': edit_form,
            'previous_link_value': previous_link,
        }

        return render(request, 'gasolina_comum/edit.html', context)
    elif request.method == 'POST':
        edit_form = forms.GasolinaComumForm(request.POST, instance=item)

        if edit_form.is_valid():
            edit_form.save()

        return redirect(previous_link)


def delete(request, pk):
    """
    Obtém o item no banco de dados, caso ele exista, e exibe as informações
    em um form não editável para o usuário, oferecendo as opções de deletar
    o item ou cancelar a operação. 
    """
    previous_link = request.GET.get('previous_link', '/')
    item = get_object_or_404(models.GasolinaComum, pk=pk)

    if request.method == 'GET':
        delete_form = forms.GasolinaComumForm(instance=item)

        context = {
            'delete_form': delete_form,
            'previous_link_value': previous_link,
        }

        return render(request, 'gasolina_comum/delete.html', context)

    elif request.method == 'POST':
        item.delete()

        return redirect(previous_link)
