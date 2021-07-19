"""Defines URL patterns for covid_life_hackers."""

from django.urls import path

from . import views

app_name = 'covid_life_hackers'
urlpatterns = [
    # Home page.
    path('', views.index, name= 'index'),
    # Page which shows all topics.
    path('topics/', views.topics, name= 'topics'),
    # Single topic details page.
    path('topics/<int:topic_id>/', views.topic, name= 'topic'),
    # Add topic.
    path('add_new_topic/', views.add_new_topic, name='add_new_topic'),
    # Add new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page to edit entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
