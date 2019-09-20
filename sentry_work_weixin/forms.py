# coding: utf-8
from django import forms


class WorkWeixinOptionsForm(forms.Form):
    key = forms.CharField(
        max_length=255,
        help_text='Work Weixin robot webhook key'
    )