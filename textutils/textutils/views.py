from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>harry</h1> <a href="https://www.instagram.com/direct/inbox/"> direct instagram</a>''')
#
# def about(request):
#     return HttpResponse("hello sunil")

# code video 7

def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

#expretion 1
# def navigation(request):
#     s = '''<h2>Navigation Bar<br></h2>
#             <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br>
#             <a href="https://www.facebook.com/">Facebook</a><br>
#             <a href="https://www.flipkart.com/">Flipkart</a><br>
#             <a href="https://www.hindustantimes.com">News</a><br>
#             <a href="https://www.google.com/">Google</a><br>
#             <a href="https://www.instagram.com/aishofficial22/">instagram</a>'''
#
#     return HttpResponse(s)


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to upper case', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!= "\r":
                analyzed = analyzed + char
        params = {'purpose': 'removed new line ', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index +1] == " " :
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'removed new line ', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("please select any operation and try agin !!")


    return render(request, 'analyze.html', params)


# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount")