from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def members(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>HelloWorld from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
def addToDo(request):
    return HttpResponse("Hello world! addTodo")