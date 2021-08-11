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
        request.session['activities'].append({
            "gold": gold,
            "place": "granja"
        })
    
    if request.POST['place'] == 'cave':
        gold = random.randint(5, 10)
        request.session['activities'].append({
            "gold": gold,
            "place": "caverna"
        })
    
    if request.POST['place'] == 'house':
        gold = random.randint(2, 5)
        request.session['activities'].append({
            "gold": gold,
            "place": "casa"
        })
    
    if request.POST['place'] == 'casino':
        gold = random.randint(0, 50)
        request.session['activities'].append({
            "gold": gold,
            "place": "casino"
        })

    if 'gold' in request.session:
        request.session['gold'] = request.session['gold'] + gold
    else:
        request.session['gold'] = gold

    if not ('log' in request.session):
        request.session['log'] = []



    return redirect('/ninja_gold')

def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/ninja_gold')

