from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmailForm
from .tasks import send_email_task

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            # Поставить задачу в очередь
            send_email_task.delay(recipient, subject, body)

            return HttpResponse("Письмо отправляется в фоне!")
    else:
        form = EmailForm()

    return render(request, 'tasks/send_email.html', {'form': form})
