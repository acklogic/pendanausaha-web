from django.shortcuts import render

def index(request):
    return render(request, 'home_page.html')

def detail_campaign(request):
    return render(request, 'detail_campaign_page.html')
