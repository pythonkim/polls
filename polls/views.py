from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    user = request.user
    context = {'latest_question_list': latest_question_list,'user':user}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return HttpResponse("Question does not exist")
    user = request.user
    context = {'question': question, 'user':user}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        user = request.user  # 유저를 가져온다는 것은? 유저 1명의 객체를 DB에서 가져오는것이다
        if user in question.voters.all():
            return redirect('/polls/')
        selected_choice.votes += 1
        selected_choice.save()

        user.point = user.point + 100 #그 유저의 포인트필드에 100을 추가 시켜주는것
        user.save() #db에 저장해라
        question.voters.add(user)

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def mylogin(request):
    print(request.user)
    if request.method == "GET":
        return render(request,'polls/login.html')
    elif request.method == "POST":
        user_id = request.POST['user_id']
        password = request.POST['password']
        print(user_id)
        print(password)

        user = authenticate(username = user_id, password = password)
        print(user)

        if user == None:
            print("아이디를 입력하세요")
            return redirect("http://naver.com")
        else:
            login(request,user) #장고세션에 유저정보를 저장, 즉 로그인한 사람임.
            return redirect("/polls/")

def data(request):
    user = request.user
    print(user)
    if user.is_authenticated: #로그인이 되었다면 True
        return render(request, 'polls/data.html')
    else: #로그인이 안되어있다면
        return redirect("/polls/login/")



def dddd(request):
    return render(request, 'polls/dddd.html')

def mylogout(request):
    logout(request) #이렇게 하면 로그아웃 됨
    return redirect('/polls/login/')




# Create your views here.
