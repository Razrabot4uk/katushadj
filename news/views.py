from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, ContactMessage, Announcement
from .forms import CommentForm, ContactForm
from django.contrib import messages

def index(request):
    upcoming_events = Event.objects.filter(is_past_event=False).order_by('event_date')
    context = {'upcoming_events': upcoming_events}
    return render(request, 'news/index.html', context)

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    comments = event.comments.filter(approved=True)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = CommentForm()
    context = {'event': event, 'comments': comments, 'form': form}
    return render(request, 'news/event_detail.html', context)

def about(request):
    return render(request, 'news/about.html')

def gallery(request):
    past_events = Event.objects.filter(is_past_event=True).order_by('-event_date')
    context = {'past_events': past_events}
    return render(request, 'news/gallery.html', context)

def contact(request):
    return render(request, 'news/contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('contact')  # Перенаправляем на ту же страницу contact после отправки формы
    else:
        form = ContactForm()
    
    return render(request, 'news/contact.html', {'form': form})

# Представление для страницы с подтверждением успешной отправки сообщения
def success_message(request):
    return render(request, 'news/success_message.html')

def announcements_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'news/announcements_list.html', {'announcements': announcements})