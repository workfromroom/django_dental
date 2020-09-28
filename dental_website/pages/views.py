from django.shortcuts import render

def index(request):
    return render(request, 'index.html',{})
def about(request):
    return render(request, 'about.html',{})
def blog(request):
    return render(request, 'blog.html',{})
def blog_details(request):
    return render(request, 'blog-details.html',{})
def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']

        send_mail(
            message_name,message,message_email,['toyeex@gmail.com'],fail_silently=False,
        )
    else:
        return render(request, 'contact.html',{})
def pricing(request):
    return render(request, 'pricing.html',{})
def service(request):
    return render(request, 'service.html',{})

