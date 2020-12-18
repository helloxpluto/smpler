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



def upload_sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST, request.FILES)
        if form.is_valid():
            sample = form.save()
            return redirect('/', pk=sample.pk)
    else:
        form = SampleForm()
    return render(request, 'smpler/sample_form.html', {'form': form})


def edit_sample(request, pk):
    sample = Sample.objects.get(pk=pk)
    if request.method == 'POST':
        form = SampleForm(request.POST, instance=sample)
        if form.is_valid():
            sample = form.save()
            return redirect('/', pk=sample.pk)
    else:
        form = SampleForm(instance=Sample)
    return render(request, 'smpler/sample_form.html', {'form': form})


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['sample']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'smpler/upload.html', context)
