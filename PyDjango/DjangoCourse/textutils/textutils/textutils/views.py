from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html' )

def about(request):
    return render(request,'about.html' )


def contact(request):
    return render(request,'contact.html' )


def analyze(request):
    btn = '''<li> <a href='/'>Back</a> </li>'''
    # Getting the text 
    dj_text = request.POST.get('text', 'default')

    # To check the checkbox value - on or off
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # Check if removepunc is on
    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for c in dj_text:
            if c not in punctuations:
                analyzed = analyzed+c;    

        if fullcaps=="on":
            params={
            'purpose':'Remove punctuations',
            'analyze_text': analyzed.upper()
        }
        else:
            params={
            'purpose':'Remove punctuations',
            'analyze_text': analyzed.lower()
        }
        dj_text=analyzed
    if (fullcaps=="on"):
        analyzed = " "
        for char in dj_text:
            analyzed = analyzed + char.upper()
        params={
        'purpose':'Changed to UPPERCASE',
        'analyze_text': analyzed
     }
        dj_text=analyzed


    if (newlineremover=="on"):
        analyzed=""
        for c in dj_text:          
            if c!='\n' and c!='\r':
                analyzed = analyzed+c;    
        params={
        'purpose':'New line removed',
        'analyze_text': analyzed
     }
        dj_text=analyzed


    if (extraspaceremover == "on"):
        analyzed=""
        for index, char in enumerate(dj_text):
            if not(dj_text[index]==" " and dj_text[index+1]==" "):
                analyzed=analyzed+char
        
        params={
            'purpose': 'Extra space Removed',
            'analyze_text':analyzed
        }
        dj_text=analyzed


    if (charcount =='on'):
        num=0
        analyzed=len(dj_text)
        for i in range(len(dj_text)):
            if i!=' ':
                num=num+1
        analyzed=num
        params={
            'purpose':'Number of characters ',
            'analyze_text':analyzed,
        }
        dj_text=analyzed

    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and charcount!='on' and extraspaceremover!='on'):
        return HttpResponse("Error")
        
    return render(request,'analyze.html', params)
 