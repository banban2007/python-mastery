from django.urls import path
from .views import *

urlpatterns = [
    path('List/',postList),
    path('create/',postCreate),
    path('delete/<int:id>/',Delete),
    path('detail/<int:id>/',postDetail),
    path('update/<int:id>/',postUpdate),
    path('login/',postLogin),
    path('cmt/create/<int:post_id>/',cmt_create),
    path('cmt/delete/<int:cid>/<int:pid>/',cmt_delete),
    path('cmt/update/<int:cid>/<int:pid>/',cmtUpdate),
    path('search/',search_by),
    path('filterby/<int:cid>/',filter_by)

]