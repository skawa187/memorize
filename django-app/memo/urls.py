from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import MemoList, MemoDetail, MemoCreate, MemoUpdate, MemoDelete, UserLoginView, SignupView, test

urlpatterns = [
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
    path('signup/', SignupView.as_view(), name = 'signup'),
    path('', MemoList.as_view(), name = 'memo-list'),
    path('memo/<int:pk>/', MemoDetail.as_view(), name = 'memo-detail'),
    path('memo-create/', MemoCreate.as_view(), name = 'memo-create'),
    path('memo-update/<int:pk>', MemoUpdate.as_view(), name = 'memo-update'),
    path('memo-delete/<int:pk>', MemoDelete.as_view(), name = 'memo-delete'),
    path('test/<int:i>', test, name = 'test')
]