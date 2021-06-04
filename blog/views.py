from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator
    

# General Methods
def paginate(request, list_objects, items_per_page):
    paginator = Paginator(list_objects, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj


# Views
def home_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    return render(request,
                  '../templates/home_page.html', 
                  {'featured_posts': posts[0:3],
                   'card_posts': posts[3:],
                   'post_1': posts[0],
                   'post_2': posts[1],
                   'post_3': posts[2],
                   'post_4': posts[3],
                   'post_5': posts[4],
                   'post_6': posts[5],
                   'post_7': posts[6],
                   }
                  )

    
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    page_obj = paginate(request, posts, 4)

    return render(request,
                  '../templates/post_list.html',
                  {'page_name': "DSCSM - Blog",
                   'page_obj': page_obj
                   }
                  )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,
                  '../templates/post_detail.html',
                  {'post': post,
                   'page_name': post.title,
                   }
                 )
