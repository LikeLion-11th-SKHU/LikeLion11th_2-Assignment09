from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule
from .forms import ScheduleForm 
from django.utils import timezone
from django.http import HttpResponse

def main(request): 
    return render(request, 'main.html')

def read(request, date=None): 
    date = request.GET.get('date')
    if date:
        try:
            schedules = Schedule.objects.filter(date=date)
        except Schedule.DoesNotExist:
            schedules = None  
        return render(request, 'read.html', {'schedules': schedules})
    else: 
        return HttpResponse("date 없음") 

def create(request):
    date = request.GET.get('date')
    if request.method == 'POST':
        form = ScheduleForm(request.POST) # request.POST에 담긴 데이터로 ScheduleForm 객체 생성
        schedule = form.save(commit=True) # form을 DB에 저장
        date = schedule.date.strftime('%Y-%m-%d') # 저장된 일정의 날짜를 가져옴
        return redirect(f'/read/?date={date}') # 저장된 일정의 날짜를 가지고 read 페이지로 이동
    else:
        form = ScheduleForm() # GET 방식으로 요청이 들어오면 빈 ScheduleForm 객체를 만들어서 create 페이지에 넘김

    return render(request, 'create.html', {'form': form, 'date': date}) # form과 date를 create 페이지에 넘김

    
def update(request, id): 
    schedule = get_object_or_404(Schedule, pk=id) # id에 해당하는 Schedule 객체를 가져옴
    if request.method == 'POST': 
        form = ScheduleForm(request.POST, instance=schedule) # request.POST에 담긴 데이터로 ScheduleForm 객체 생성
        form = form.save(commit=True) # form을 DB에 저장
        date = form.date.strftime('%Y-%m-%d')  # 수정된 일정의 날짜를 가져옴
        return redirect(f'/read/?date={date}')  # 수정된 일정의 날짜를 가지고 read 페이지로 이동
    elif request.method == 'GET': 
        form = ScheduleForm(instance=schedule) # GET 요청시 id에 맞는 Schedule 객체를 form에 담아 update에 넘김
    
    return render(request, 'update.html', {'form': form, 'schedule': schedule}) # form, schedule을 update에 넘김

def delete(request, id):
    schedule = get_object_or_404(Schedule, pk=id) 
    schedule.delete()
    return redirect('main')

