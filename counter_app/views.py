from django.shortcuts import render, redirect

def index(request):
    if 'index' and 'visits' in request.session:
        print(request.session['index'])
        request.session['index'] += 1
        request.session['visits'] += 1
    else:
        request.session['index'] = 0
        request.session['visits'] = 0
    return render(request, 'index.html')

def destroy(request):
    del request.session['index']
    return redirect('/')

def add_two(request):
    request.session['index'] += 1
    return redirect('/')

def increment(request):
    request.session['index'] += (int(request.GET['increment'])-1)
    return redirect('/')