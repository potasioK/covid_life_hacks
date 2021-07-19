from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """Home page for Covid Life Hacks."""
    return render(request, 'covid_life_hackers/index.html')

def topics(request):
    """Shows all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('text')
    context = {'topics': topics}
    return render(request, 'covid_life_hackers/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show individual topics and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'covid_life_hackers/topic.html', context)

@login_required
def add_new_topic(request):
    # User adds new topic
    if request.method != 'POST':
        # Create blank form.
        form = TopicForm()
    else:
        # POST data, topic exists
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('covid_life_hackers:topics')
    # Display blank form
    context = {'form': form}
    return render(request, 'covid_life_hackers/add_new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # Nothing submitted; create a blank form.
        form =EntryForm()
    else:
        # POST and process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('covid_life_hackers:topic', topic_id=topic_id)
    
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'covid_life_hackers/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        # Initial request; pre-fill form with current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted, process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('covid_life_hackers', topic_id=topic.id)
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'covid_life_hackers/edit_entry.html', context)
            
        
        
