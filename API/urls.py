from django.urls import path,include
from .views import UserView, QuestionView,TagView, AnswerView, ReplyView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user',UserView)
router.register('question',QuestionView)
router.register('answer',AnswerView)
router.register('comment',ReplyView)
router.register('tag',TagView)

#9835703460
#KBC891
urlpatterns = [
    path('api/',include(router.urls)),
    path('',views.homeView,name='Home')
]