from random import randint

import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Test, TestAnswer, FacebookUser


class TestListView(ListView):
    model = Test
    context_object_name = 'tests'
    paginate_by = 20
    template_name = 'facetests/test_list.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        query = Test.objects.all()

        if q:
            query = query.filter(name__icontains=q)

        return query


class TestDetailView(DetailView):
    model = Test
    context_object_name = 'test'
    template_name = 'facetests/test_detail.html'


class TestAnswerView(View):

    def get(self, request, slug, id):
        answer = TestAnswer.objects.get(user__id=id, test__slug=slug)
        return render(request, 'facetests/test_answer.html',
                      {'answer': answer})

    def post(self, request, slug):
        test = get_object_or_404(Test, slug=slug)

        access_token = request.POST.get('token')
        if not access_token:
            return redirect('test:test_detail', args=(slug,))

        user_data = requests.get('https://graph.facebook.com/v2.8/me',
                                 params={
                                    'access_token': access_token,
                                    'fields': 'id,name,gender,email,birthday'
                                }).json()
        user = FacebookUser(
            id=user_data['id'],
            name=user_data['name'],
            gender=user_data['gender'],
            access_token=access_token
        )

        if 'email' in user_data:
            user.email = user_data['email']
        if 'birthday' in user_data:
            user.birthday = user_data['birthday']

        user.save()

        try:
            answer = TestAnswer.objects.get(user__id=user.id, test__slug=slug)
        except TestAnswer.DoesNotExist:
            answer = TestAnswer(user=user, test=test)

        answer.option=test.options.all()[randint(0, test.options.count()-1)]
        answer.save()

        return redirect('tests:view_test_answer', slug, user.id)
