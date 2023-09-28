from django.shortcuts import render,reverse, get_object_or_404
from django.http import HttpResponseRedirect
from college_detail.forms import CollegeDetailForm
from college_detail.models import CollegeDetail
from django.contrib import messages

# Create your views here.


def college_home(request):
    # return HttpResponse("hello college home")
    data= CollegeDetail.objects.all().order_by("-id")
    context={"data":data}
    return render(request, "c_home.html", context)
def add_college(request):
    forms= CollegeDetailForm(request.POST or None, request.FILES or None)
    if forms.is_valid():
        obj = forms.save(commit=False)
        obj.user= request.user
        forms.save()
        messages.add_message(request, messages.INFO, "Your college create successfully.")
        return HttpResponseRedirect(reverse("college_detail:home"))
    context = {"form":forms}
    return render(request, "add_college.html", context)
def edit_college(request, college_id):
    college=get_object_or_404(CollegeDetail, id= college_id, user=request.user)
    form=CollegeDetailForm(request.POST or None, request.FILES or None, instance=college)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, "Your College Detail Change Succesfully.")
        return HttpResponseRedirect(reverse("college_detail:home"))
    context={"form": form}
    return render(request, "edit.html", context )

def delete_college(request):
    college_id = request.POST.get("college_id")
    post = get_object_or_404(CollegeDetail, id=college_id, user = request.user)
    post.delete()
    return HttpResponseRedirect(reverse("college_detail:home"))
