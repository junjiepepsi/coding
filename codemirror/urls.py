#-*- coding:utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('codemirror.views',
    url(r'^dirlist.html$', 'dirlist'),
    url(r'^index.html$', 'index'),
    url(r'^$', 'index'),
    url(r'^openfile.html$', 'openfile'),
    url(r'^savefile.html$', 'savefile'),
    url(r'^createfile.html$', 'createfile'),
    
) 
 
