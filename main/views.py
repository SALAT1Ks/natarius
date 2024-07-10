from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserInputForm

def index(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            phone_input = form.cleaned_data['phone_input']
            fio_input = form.cleaned_data['fio_input']
            print("Первое поле:", phone_input)  # выводим первый введенный текст в консоль
            print("Второе поле:", fio_input)

    else:
        form = UserInputForm()

    return render(request, 'main/index.html', {'form': form})


def about(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            phone_input = form.cleaned_data['phone_input']
            fio_input = form.cleaned_data['fio_input']
            print("Первое поле:", phone_input)  # выводим первый введенный текст в консоль
            print("Второе поле:", fio_input)

    else:
        form = UserInputForm()

    return render(request, 'main/about.html', {'form': form})

def tariffy(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            phone_input = form.cleaned_data['phone_input']
            fio_input = form.cleaned_data['fio_input']
            print("Первое поле:", phone_input)  # выводим первый введенный текст в консоль
            print("Второе поле:", fio_input)

    else:
        form = UserInputForm()

    return render(request, 'main/tariffy.html', {'form': form})

def required_documents(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            phone_input = form.cleaned_data['phone_input']
            fio_input = form.cleaned_data['fio_input']
            print("Первое поле:", phone_input)  # выводим первый введенный текст в консоль
            print("Второе поле:", fio_input)

    else:
        form = UserInputForm()

    return render(request, 'main/required_documents.html', {'form': form})

def contacts(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            phone_input = form.cleaned_data['phone_input']
            fio_input = form.cleaned_data['fio_input']
            print("Первое поле:", phone_input)  # выводим первый введенный текст в консоль
            print("Второе поле:", fio_input)

    else:
        form = UserInputForm()

    return render(request, 'main/contacts.html', {'form': form})

