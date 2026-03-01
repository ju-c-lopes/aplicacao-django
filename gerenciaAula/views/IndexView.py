from django.shortcuts import render


def index_view(request):
    return render(request, "index/index.html", status=200)


def sitemap_view(request):
    return render(request, "sitemap.xml", content_type="application/xml", status=200)
