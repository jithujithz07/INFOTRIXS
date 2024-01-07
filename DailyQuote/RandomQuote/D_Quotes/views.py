from django.shortcuts import render
import requests
import random

# for displaying random quotes
def Quotes(request):
    quotable_api = "https://api.quotable.io/random"
    try:
        #getting data from quotable
        response = requests.get(quotable_api)
        response.raise_for_status()
        quote_data = response.json()
        
        #saving it into a dictinary
        data = {
            'content': quote_data['content'],
            'author': quote_data['author'],
        }
        
        #redering the webpage with thw data
        return render(request,'index.html',{"data":data})

    except requests.exceptions.RequestException as e:
        print(e)
        
        
    return render(request,'index.html')

# for finding author's content using their name
def Authors(request):
    if request.method == 'POST':
        auth_name= request.POST.get('Authour', '').lower()
        quotable_api = f"https://api.quotable.io/quotes?author={auth_name}"
        try:
            #get the results from api
            response = requests.get(quotable_api)
            response.raise_for_status()
            author_data = response.json()
            data=author_data.get('results', [])
            if data:
                #choosing a random quote to show
                random_quote = random.choice(data)
                context = {
                    'quote_content': random_quote['content'],
                    'quote_author': random_quote['author'],
                }
                #rendering the result page
                return render(request,'Author_name.html',{"context":context})
            else:
                nores="oh ohhh! No person here"
                return render(request,'Author_name.html',{"nores":nores})
        except requests.exceptions.RequestException as e:
            print(e)
            
    return render(request,'Author_name.html',)