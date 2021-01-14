from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def post_list(request):
    '''
    Read(R)
    포스트들을 불러와서 리스트형태로 보여준다
    '''

    posts = Post.objects.all() #포스트옵젝에서 가져온 모든 내용을 posts에 넣음
    ctx = {'posts' : posts} #딕셔너리. 문자열 호출하면 posts라는 변수를 가져오겠다
          #왼쪽 posts는 html로 넘어가는 string, 오른쪽은 객체

    return render(request, template_name='posts/list.html', context=ctx)

def post_detail(request, post_id):
    '''
    Read(R)
    특정 포스트를 불러와서 상세정보를 보여준다
    '''
    post=Post.objects.get(id=post_id)
    ctx={'post':post}

    return render(request, template_name='post/detail.html')