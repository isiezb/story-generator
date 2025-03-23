from app import create_app
from flask import Response
import json

app = create_app()

def handle_request(request):
    """Handle incoming requests from Cloudflare Workers"""
    # Convert Cloudflare request to WSGI environment
    environ = {
        'REQUEST_METHOD': request.method,
        'PATH_INFO': request.url.split('?')[0],
        'QUERY_STRING': request.url.split('?')[1] if '?' in request.url else '',
        'wsgi.input': request.body,
        'wsgi.errors': None,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input_terminated': True,
    }

    # Add headers
    for key, value in request.headers.items():
        environ[f'HTTP_{key.upper().replace("-", "_")}'] = value

    # Process the request through Flask
    response = app(environ, lambda status, headers: None)
    
    # Convert Flask response to Cloudflare response
    status = response[0]
    headers = dict(response[1])
    body = b''.join(response[2])

    return Response(
        body,
        status=status,
        headers=headers
    )

def main(request):
    """Main entry point for Cloudflare Workers"""
    return handle_request(request) 