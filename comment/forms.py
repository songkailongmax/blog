"""
@author: songkailong
@file: forms.py
@time: 2020/8/8 16:46
@software: PyCharm
"""

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
