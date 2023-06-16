def get_site_url(request):
    
    url = request.get_full_path()
    url_elem = [endpoint for endpoint in url.split('/') if endpoint and endpoint.startswith("?") !=True]
    return { 'url': url_elem, 'full_url':url }