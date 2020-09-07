from django.shortcuts import render
import json
import requests
# Create your views here.

def news(request):
    news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    news = json.loads(news_request.content)
    return render(request, 'news.html', {'news': news})


def prices(request):
    prices_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,XRP,DOT,LINK,BCH,LTC,BNB,CRO&tsyms=USD,EUR")
    prices = json.loads(prices_request.content)
    return render(request, 'prices.html', {'prices': prices})


def lookup(request):
    if request.method == 'POST':
        searchValue = request.POST['searchValue']
        searchValue = searchValue.upper()
        search_result_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + searchValue + "&tsyms=USD")
        search_result = json.loads(search_result_request.content)
        return render(request, 'lookup.html', {'search_result': search_result, 'searchValue': searchValue})
