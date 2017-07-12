import json

from django.shortcuts import render
from sitters.models import Sitter


def index(request):
    sitters = Sitter.objects.all().order_by('-overall_rank')
    context = {
        'sitters': sitters,
        'sitters_json': json.dumps([{
            'name': sitter.name,
            'image': sitter.image,
            'overall_rank': sitter.overall_rank
        } for sitter in sitters])
    }
    return render(request, 'index.html', context)


