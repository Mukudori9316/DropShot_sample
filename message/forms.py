from django import forms
from . import models
from .get_member import GetMember


class MessageForm(forms.Form):
    message = forms.CharField(
        label='メッセージ',
        max_length=255,
        required=None,
        widget=forms.Textarea(),
    )
    author = forms.ModelChoiceField(
        models.Member.objects.values_list('name', flat=True),
        empty_label='------',
        label='投稿者',
        required=True,
        to_field_name="name",
    )
    create_for = forms.ModelChoiceField(
        models.Member.objects.values_list('name', flat=True),
        empty_label='------',
        label='相手',
        required=True,
        to_field_name="name",
    )


class MemberForm(forms.Form):
    YEAR_CHOICES = GetMember.year_choices
    NAME_CHOICES = GetMember.name_choices
    year = forms.CharField(
        label='学年',
        required=True,
        widget=forms.Select(choices=YEAR_CHOICES)
    )
    name = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.Select(choices=NAME_CHOICES)
    )


class SendForm(forms.Form):
    YEAR_CHOICES = GetMember.year_choices
    NAME_CHOICES = GetMember.name_choices
    message = forms.CharField(
        label='メッセージ',
        max_length=255,
        required=None,
        widget=forms.Textarea(),
    )
    create_for = forms.ModelChoiceField(
        models.Member.objects.values_list('name', flat=True),
        empty_label='------',
        label='相手',
        required=True,
        to_field_name="name",
    )
