from django.shortcuts import render, redirect
from .forms import VideoUploadForm
from .models import Video, Index

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            # Extract subtitles and create indexes using CCExtractor
            # Save the indexes to the database
            # You can use CCExtractor library to perform this step

            return redirect('video_detail', video_id=video.id)
    else:
        form = VideoUploadForm()
    return render(request, 'upload_video.html', {'form': form})

def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    indexes = Index.objects.filter(video=video)
    return render(request, 'video_detail.html', {'video': video, 'indexes': indexes})

def search(request):
    keyword = request.GET.get('keyword')
    indexes = Index.objects.filter(subtitle__icontains=keyword)
    return render(request, 'search_results.html', {'keyword': keyword, 'indexes': indexes})
