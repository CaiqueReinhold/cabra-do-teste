from django.db.models import Count

from .models import Test


def popular_tests(request):
    tests = (Test.objects.all().
             annotate(answers=Count('testanswer')).
             order_by('-answers'))[:5]
    return {'popular_tests': tests}
