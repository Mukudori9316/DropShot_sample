from django import forms
from .get_member import GetMember


class MessageForm(forms.Form):
    YEAR_CHOICES = GetMember.year_choices
    NAME_CHOICES = GetMember.name_choices
    message = forms.CharField(
        label='メッセージ',
        max_length=255,
        required=None,
        widget=forms.Textarea(),
    )
    author = forms.CharField(
        label='投稿者',
        max_length=20,
        required=True,
        widget=forms.Select(choices=NAME_CHOICES),
    )
    create_for = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.Select(choices=NAME_CHOICES)
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
    create_for = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.Select(choices=NAME_CHOICES)
    )
