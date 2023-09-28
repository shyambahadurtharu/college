from django.shortcuts import render, reverse, get_object_or_404
# from post.models import Post
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from post.models import Post, Like
from post.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_feed(request):
    posts = Post.objects.all().order_by("-id")
    
    user_name = request.user.username.upper()
    
    context ={
        "posts":posts,
        "user_name":user_name
    }
    return render(request, "home_feed.html", context)
@login_required
def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # print(form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        form.save()
        return HttpResponseRedirect(reverse("post:home"))
    context = {"form": form}
    return render(request, "add_post.html", context)
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user = request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("post:home"))
    context= {"form":form}
    return render(request, "edit_post.html", context)
@login_required 
def delete_post(request):
    post_id = request.POST.get("post_id")
    post = get_object_or_404(Post, id=post_id, user = request.user)
    post.delete()
    return HttpResponseRedirect(reverse("post:home"))
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    like, created= Like.objects.get_or_create(
        post=post, 
        user=user,
        defaults={"is_liked":True}
     )
    if not created:
        if like.is_liked:
            like.is_liked = False
        else:
            like.is_liked = True
        like.save()
    
    return JsonResponse({"is_liked":like.is_liked, "like_count": post.like_count}, safe=False)

@login_required(login_url="/post:comment_post/")
def comment_post(request, post_id):
    

    post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.all() #Comment.objects.filter(post__id=post_id)
    
    form = CommentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.post = post
        obj.user = request.user
        obj.comment_image = request.POST.get('comment_image')
        obj.save()
       
        return HttpResponseRedirect(reverse("post:comment_post", args=(post_id, )))
    context = {"post":post, "comments":comments, "form": form}
    return render(request, "post_comment.html", context)
