# -*- coding: utf-8 -*-
from django.shortcuts import render
import requests,json

def chart_issues(request):
    issues_create = []
    if request.GET:
        url = request.GET['target']
        url_contir = 'https://api.github.com/repos/' + url +'/issues'
        s = requests.session()
        s.keep_alive = False
        r = requests.get(url_contir)
        resps = r.json()
        
        issues_created = 0
        issues_closed = 0
        # 获取每个issue信息
        for resps in resps:
            issues_created = issues_created + 1
            issues_state = resps['state']
            if issues_state is "closed":
                issues_closed = issues_closed + 1
    else:
        issues_created = 0
        issues_closed = 0
    issues_create.append(issues_created)
    issues_create.append(issues_closed)
    return render(request,'issues.html', {"issues_create": issues_create} )