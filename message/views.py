from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Message
from .models import Member
from .forms import MessageForm, SendForm
from .get_member import GetMember


def index(request):
    d = {
        "messages": Message.objects.all(),
        "members": Member.objects.all(),
    }
    return render(request, "index.html", d)


def add(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        author = Member.objects.get(name=form.cleaned_data['author'])
        create_for = (
            Member.objects.get(name=form.cleaned_data['create_for']))
        Message.objects.create(
            message=form.cleaned_data['message'],
            author=author,
            create_for=create_for,
        )
        # **:可変長引数 / form.cleaned_data: バリデーションを通過したデータが入ってる
        """今回のデータはMessageeクラスで定義されたmessageとcreated_at
            class Message(models.Model):
            message = models.CharField(max_length=255)
            created_at = models.DateTimeField(auto_now_add=True)"""
        return redirect('message:index')
    d = {
        'message_form': form,
    }
    return render(request, 'edit.html', d)


def edit(request, editing_id):
    message = get_object_or_404(Message, id=editing_id)
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message.is_valid():
            author = Member.objects.get(name=message.cleaned_data['author'])
            create_for = (
                Member.objects.get(name=message.cleaned_data['create_for']))
            Message.objects.create(
                message=message.cleaned_data['message'],
                author=author,
                create_for=create_for,
            )
            return redirect('message:index')
    else:
        # GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
        message_form = MessageForm(
            {'message': message.message,
             'author': message.author.name,
             'create_for': message.create_for.name,
             })
    d = {
        'message_form': message_form,
    }

    return render(request, 'edit.html', d)


@require_POST
def delete(request):
    delete_ids = request.POST.getlist('delete_ids')
    if delete_ids:
        Message.objects.filter(id__in=delete_ids).delete()
    return redirect('message:index')


def dropshot(request):
    d = {
        'messages': Message.objects.all(),
        'members': Member.objects.all(),
    }
    return render(request, 'dropshot.html', d)


def add_all(request):
    def save(year, name):
        data = Member(name=name, year=year)
        data.save()
        return()
    for member in GetMember.members:
        name = member[1]
        year = member[0]
        save(year, name)
    return redirect('message:index')


def get_message(request, member_id):
    master = Member.objects.get(id=member_id)
    name = master.name
    messages = Message.objects.filter(create_for=name)
    form = SendForm(request.POST or None)
    if form.is_valid():
        create_for = (
            Member.objects.get(name=form.cleaned_data['create_for']))
        Message.objects.create(
            message=form.cleaned_data['message'],
            author=master,
            create_for=create_for,
        )
        return redirect('message:get_message', member_id)
    d = {
        'messages': messages,
        'name': name,
        'send_form': form,
    }
    return render(request, 'member_page.html', d)


def top(request):
    return render(request, 'top.html')


def top2(request):
    return render(request, 'top2.html')
