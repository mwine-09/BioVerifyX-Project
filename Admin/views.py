from django.shortcuts import render

# Create your views here.





def showAdminIndex(request):

    return render(request,'Admin/index.html')
