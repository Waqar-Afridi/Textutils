# i have created this file -waqar
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    # get the text
    djtext=(request.POST.get('text', 'default'))
    print(djtext)

    #checkboxes ki jo b value hai osko check karo
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    counter = request.POST.get('counter', 'off')

 # konsa checkbox on hai
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'extraspaceremover', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        # return render(request, 'analyze.html', params)

    if(counter=="on"):
        analyzed = 0
        for char in djtext:
            if char.isalpha():
                analyzed=analyzed+1


        params = {'purpose': 'charounter', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        # return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre",analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps!="on" and extraspaceremover != "on" and newlineremover!="on" and counter!="on"):
        return HttpResponse("Please select any operation and try again.")

    return render(request, 'analyze.html', params)


