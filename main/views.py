from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Student, Reja
from .forms import RejaForm

def studentlar(request): return HttpResponse('<br>'.join(f'{s.id}. {s.ism} | {s.yosh} | {s.kurs}' for s in Student.objects.all()) or 'Studentlar mavjud emas.')
def rejalar(request): return HttpResponse('<br>'.join(f'{r.id}. {r.sarlavha} | {r.student.ism} | {r.sana} | {r.bajarildi}' for r in Reja.objects.select_related('student')) or 'Rejalar mavjud emas.')
def bajarilmagan_rejalar(request): return HttpResponse('<br>'.join(f'{r.id}. {r.sarlavha} | {r.student.ism} | {r.sana}' for r in Reja.objects.filter(bajarildi=False).select_related('student')) or 'Bajarilmagan rejalar mavjud emas.')
def bitiruvchilar(request): return HttpResponse('<br>'.join(f'{s.id}. {s.ism} | {s.yosh} | {s.kurs}' for s in Student.objects.filter(kurs__gte=3)) or 'Bitiruvchilar mavjud emas.')
def kattalar(request): return HttpResponse('<br>'.join(f'{s.id}. {s.ism} | {s.yosh} | {s.kurs}' for s in Student.objects.filter(yosh__gt=20)) or '20 yoshdan katta studentlar mavjud emas.')
def bitiruvchilar_rejalari(request): return HttpResponse('<br>'.join(f'{r.id}. {r.sarlavha} | {r.student.ism} | {r.sana}' for r in Reja.objects.filter(student__kurs__gte=3).select_related('student')) or 'Rejalar mavjud emas.')
def talaba_rejalari(request,talaba_id):
    s=get_object_or_404(Student,id=talaba_id)
    return HttpResponse('<br>'.join(f'{r.id}. {r.sarlavha} | {r.sana} | {r.bajarildi}' for r in Reja.objects.filter(student=s)) or f'{s.ism} uchun reja yo‘q.')
def reja_ochirish(request,reja_id):
    r=get_object_or_404(Reja,id=reja_id)
    if request.method=='POST': r.delete(); return redirect('rejalar')
    return HttpResponse(f'<form method="post">{request.csrf_processing_done if False else ""}<p>{r.sarlavha}</p><button>O‘chirish</button></form>')
def reja_qoshish(request):
    if request.method=='POST':
        f=RejaForm(request.POST)
        if f.is_valid(): f.save(); return redirect('rejalar')
    else: f=RejaForm()
    return HttpResponse(str(f))
