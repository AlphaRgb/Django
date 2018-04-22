from django.shortcuts import render

def book_list(request):
	return render(request,'blogs/mobile_list.html',{})