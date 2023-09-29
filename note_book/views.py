from django.shortcuts import render
from note_book.forms import NoteForm
# Create your views here.
from django.http import JsonResponse
from note_book.models import Semester
def home(request):
    return render(request, "home.html")
def add_note(request):
    form = NoteForm(request.POST or None, request.FILES or None)
    context={'form':form}
    return render(request,"add_note.html", context)

def get_semester(request):
    level_id = request.GET.get('level_id')
    semester = Semester.objects.filter(level=level_id)
    semester_list = [{'id': semester.id, 'name': semester.name} for semester in semester]
    return JsonResponse({'semesters': semester_list})