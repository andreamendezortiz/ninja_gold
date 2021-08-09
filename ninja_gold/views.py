from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    

    context = {
        'gold': request.session['gold']
    }

    return render(request, 'index.html', context)



def process_money(request):

    if request.POST['place'] == 'farm':
        gold = random.randint(10, 20)
    
    if request.POST['place'] == 'cave':
        gold = random.randint(5, 10)
    
    if request.POST['place'] == 'house':
        gold = random.randint(2, 5)
    
    if request.POST['place'] == 'casino':
        gold = random.randint(0, 50)

    if 'contador' in request.session:
        request.session['contador'] = request.session['contador'] + gold
    else:
        request.session['contador'] = gold

    if not ('log' in request.session):
        request.session['log'] = []



    return redirect('/ninja_gold')

def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/ninja_gold')

