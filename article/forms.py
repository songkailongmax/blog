"""
@author: songkailong
@file: forms.py
@time: 2020/8/3 16:34
@software: PyCharm
"""

from django import forms
from .models import ArticlePost


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title', 'body')
