# -*- coding: utf-8 -*-
from django.shortcuts import render
import requests

def Contribution_from(request):
    contribute_datas = []
    if request.GET:
        url = request.POST['url1']
        u_list = url.strip().split('/')
        url_contir = 'https://api.github.com/repos/' + u_list[3]+'/'+u_list[4] +'/contributors'
        print(url_contir)
        s = requests.session()
        s.keep_alive = False
        r = requests.get(url_contir)
        resps = r.json()
        for resps in resps:
            contribute_data = {
                'value':resps['contributions'],
                'name':resps['login']
            }
            contribute_datas.append(contribute_data)
    else:
        contribute_datas = []

    return render(request,'contribution.html', {"contribute_datas": contribute_datas} )