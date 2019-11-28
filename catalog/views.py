from django.shortcuts import render


from .models import Ruler, Material, Nominal, Coin, MD, MCM, Redkost
####### Функция отображения для домашней страницы сайта.
def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_coins=Coin.objects.all().count()
    num_rules=Ruler.objects.all().count()
    num_filter=Ruler.objects.filter(name__contains='г').count()
    # Доступные книги (статус = 'a')
    #num_instances_available=BookInstances.objects.filter(status__exact='a').count()
    num_nominal=Nominal.objects.count()  # Метод 'all()' применен по умолчанию.
    # Отрисовка HTML-шаблона index.html с данными внутри переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_coins':num_coins,
                 'num_rules':num_rules,
                 'num_nominal':num_nominal,
                 'num_filter':num_filter,},
    )

from django.views import generic

class CoinListView(generic.ListView):
    model = Coin
    template_name = 'coins-list.html'  # Определение имени вашего шаблона и его расположения

class CoinDetailView(generic.DetailView):
    model = Coin
    template_name = 'coin-detail.html'  # Определение имени вашего шаблона и его расположения

# class CoinListSFilterView(generic.ListView):
#     model = Coin
#     template_name = 'coins-list-sfilter.html' 


class RulersListView(generic.ListView):
    model = Ruler
    template_name = 'rulers-list.html'  # Определение имени вашего шаблона и его расположения

class RulersDetailView(generic.DetailView):
    model = Ruler
    template_name = 'ruler-detail.html'  # Определение имени вашего шаблона и его расположения