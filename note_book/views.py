from django.shortcuts import render, HttpResponseRedirect, reverse
from note_book.forms import NoteForm
from note_book.models import Level, NoteBook
# Create your views here.
from django.http import JsonResponse
from note_book.models import Semester
from django.core.files.storage import FileSystemStorage
def home(request):
    level=Level.objects.all()
    notebook=NoteBook.objects.all()
    context={"level":level, "notebook":notebook}
    return render(request, "home.html", context)
def add_note(request):
    level=Level.objects.all().order_by('-id')
    if request.method == 'POST':
        uploaded_file = request.FILES['pdf_file']
        
        # You can save the file, process it, or do whatever you need
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        # Get the level_id from the form data
        
        course=request.POST.get("cousre_name")
        level_id = request.POST.get('level')
             
        semester_id=request.POST.get("semester")
        
            # Try to retrieve the Level instance based on the level_id
        level_instance = Level.objects.get(id=level_id)
        semester_instance = Semester.objects.get(id=semester_id)
        
            # Create a new NoteBook instance and associate it with the Level instance
        item=NoteBook(file_upload=filename, course_name=course, level_id=level_instance, semester_id=semester_instance)
        item.save()

            # Redirect to a success page or do whatever is needed
        return HttpResponseRedirect(reverse("note_book:note_home"))

        

    context={'level':level}
    return render(request,"add_note.html", context)
def get_semester(request):
    level_id = request.GET.get('level_id')
    semester = Semester.objects.all().filter(level=level_id)
    semester_list = [{'id': semester.id, 'name': semester.semester_name} for semester in semester]
    return JsonResponse({'semesters': semester_list})

 