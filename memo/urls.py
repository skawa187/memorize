from django.urls import path
from .views import MemoList, MemoDetail, MemoCreate, MemoUpdate, MemoDelete

urlpatterns = [
    path('', MemoList.as_view(), name = 'memo-list'),
    path('memo/<int:pk>/', MemoDetail.as_view(), name = 'memo-detail'),
    path('memo-create/', MemoCreate.as_view(), name = 'memo-create'),
    path('memo-update/<int:pk>', MemoUpdate.as_view(), name = 'memo-update'),
    path('memo-delete/<int:pk>', MemoDelete.as_view(), name = 'memo-delete'),
]