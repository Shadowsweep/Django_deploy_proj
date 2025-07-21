from django.shortcuts import render, redirect
from .forms import EntryForm
from .models import Entry

def home(request):
    """
    Renders the home page with options to view and create entries.
    """
    return render(request, 'home.html')

def add_entry(request):
    """
    Handles adding new entries.
    - If GET request, displays an empty form.
    - If POST request, validates and saves the form data.
    """
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save() # Save the new entry to the database
            return redirect('entry_list') # Redirect to the list view after successful submission
    else:
        form = EntryForm() # Create an empty form for GET requests
    return render(request, 'entry_form.html', {'form': form})

def entry_list(request):
    """
    Displays a list of all existing entries.
    """
    entries = Entry.objects.all().order_by('-created_at') # Retrieve all entries, ordered by creation date
    return render(request, 'entry_list.html', {'entries': entries})