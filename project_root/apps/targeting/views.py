```python
from django.shortcuts import render
from .models import TargetArea

def index(request):
    target_areas = TargetArea.objects.all()
    return render(request, 'targeting/index.html', {'target_areas': target_areas})

def detail(request, target_area_id):
    target_area = TargetArea.objects.get(id=target_area_id)
    return render(request, 'targeting/detail.html', {'target_area': target_area})
```