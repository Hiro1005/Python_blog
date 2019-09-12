from django.template.response import TemplateResponse

from guestbook.forms import GreetingForm
from guestbook.models import Greeting
from random import choice

title = 'Hiro の GuestBook(django)'
sub_titles = ['How are you?', 'Sayang Sayang.', 'How is weather?']

def index(request):

    sub_title = choice(sub_titles)

    """メイン画面."""
    if request.method == 'POST':
        form = GreetingForm(request.POST)
        if form.is_valid():
            # データの新規追加
            form.save()
    else:
        form = GreetingForm()

    greetings = Greeting.objects.order_by('-created_at')[:5]
    return TemplateResponse(request,
                            'guestbook/index.html',
                            {'greetings': greetings,
                             'form': form,
                             'title': title,
                             'sub_title': sub_title})