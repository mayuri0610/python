# views.py
from django.shortcuts import render, redirect
from .utils import bulk_create_persons_from_csv
from .forms import PersonBulkUploadForm  # If you have created a form

def upload_csv(request):
    if request.method == 'POST':
        form = PersonBulkUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file_upload']
            bulk_create_persons_from_csv(csv_file)
            return redirect('success_url')  # Redirect to a success page
    else:
        form = PersonBulkUploadForm()  # Create an instance of your form
    return render(request, 'index.html', {'form': form})
