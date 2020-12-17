from django.shortcuts import render, redirect
from .models import Sample
from .forms import SampleForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# Create your views here.

@login_required


def sample_list(request):
    samples = Sample.objects.all()
    return render(request, 'smpler/sample_list.html', {'samples': samples})


def sample_detail(request, pk):
    sample = Sample.objects.get(id=pk)
    return render(request, 'smpler/sampler_detail.html', {'sample': sample})

def sample_play(request, playsound, pk):
    sample = Sample.objects.get(id=pk)
    return playsound('sample_play', pk=sample.pk)

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['sample']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'smpler/upload.html')
