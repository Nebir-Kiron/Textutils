# i have created this file ---> kiron
from django.http import HttpResponse
from django.shortcuts import render

#code for video 6
#def index(request):
#    return HttpResponse('''<h1>hello kiron bhai<h1/> 
#    <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> django video </a> <br>
#
#    <a href="https://www.youtube.com/">go to youtube </a>
#    ''')
#
#
#def about(request):
#    return HttpResponse('hi i am about')



# code for video 7 (laying the pipeline)
def index(request):
    return render(request,'index.html')


def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    rempunc = request.POST.get('removepunc','off')
    upcas = request.POST.get('fullcaps','off')
    newline_remover = request.POST.get('newlinermv','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    countchar = request.POST.get('countchar','off')
    panctuations = '''!()-[]{};:'"/\|<>,.?@#$%^&*'''


    if True:
        if rempunc=='on': 
            analyzed = ""
            for i in djtext:
                if i not in panctuations:
                    analyzed+=i
            prams = {'purpose':'Remove punctuations','analyzed_text':analyzed}
            djtext = analyzed



        if upcas=='on':
            analyzed = ""
            for i in djtext:
                if i not in panctuations:
                    analyzed += i.upper()
            prams = {'purpose':'change to upper case','analyzed_text':analyzed}
            djtext = analyzed
  
   

        if newline_remover=='on':
            analyzed = ""
            for i in djtext:
                if i != '\n' and i!='\r':
                    analyzed += i
            prams = {'purpose':'removing newline','analyzed_text':analyzed}
            djtext=analyzed
   


        if extraspaceremover=='on':
            analyzed = ""
            for index,i in enumerate(djtext):
                if not (djtext[index]==' ' and djtext[index+1]==' '):
                    analyzed += i
            prams = {'purpose':'removing Extraspace','analyzed_text':analyzed}
            djtext=analyzed
     




        

        if rempunc=='off' and upcas=='off' and newline_remover=='off' and extraspaceremover=='off':
            return HttpResponse('<h3>Error</h3> <a href="/">Back</a>')
       
        return render(request,'analyze.html',prams)



       




    
