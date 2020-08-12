"""
@author: songkailong
@file: urls.py
@time: 2020/8/8 16:36
@software: PyCharm
"""

from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('post_comment/<int:article_id>/', views.post_comment, name='post_comment'),
    path('post-comment/<int:article_id>/<int:parent_comment_id>', views.post_comment, name='comment_reply')

]
