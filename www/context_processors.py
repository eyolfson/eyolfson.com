def canonical(request):
    return {
        "CANONICAL": request.build_absolute_uri(request.path),
    }
