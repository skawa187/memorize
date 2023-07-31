from django.urls import path
from .views import MemoList, MemoDetail

urlpatterns = [
    path('', MemoList.as_view(), name = 'memo_list'),
    path('memo/<int:pk>/', MemoDetail.as_view(), name = 'memo_detail')
]