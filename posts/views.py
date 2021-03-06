from urllib import quote_plus
from django.utils.encoding import smart_str, smart_unicode
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Post

from .forms import PostForm

# Create your views here.
#render returns html content
#view handles whats sent to it from admin urls

def posts_create(request):
	#gets rid of validation text
	form = PostForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# method success
		messages.success(request,"Successfully Created")

		return HttpResponseRedirect(instance.get_absolute_url())


	# if request.method == "POST":
	# 	print request.POST.get("content")
	# 	print request.POST.get("title")

	context_data = {

		"form":form,
	}

	return render(request,"post_form.html",context_data)

def posts_update(request,id=None):
	#combines post_detail with post_create

	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags ='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context_data = {
		"title":instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "post_form.html", context_data)


def posts_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	share_string = quote_plus(smart_str(instance.content))
	context_data = {
		"title":instance.title,
		"instance": instance,
		"share_string": share_string,
		
	}

	return render(request, "posts_detail.html", context_data)

def posts_delete(request, id = None):
	instance = get_object_or_404(Post, id = id)
	instance.delete()
	messages.success(request, "Successfully Deleted")

	return redirect("posts:list")



def posts_list(request):
	queryset_list = Post.objects.all()
	# .order_by("-timestamp")
	paginator = Paginator(queryset_list, 25)

	page = request.GET.get('page')
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)

	context_data = {
			"object_list": queryset,
			"title" : "Posts",

	}

	return render(request, "posts_list.html", context_data)



#authenticated user code
		# if request.user.is_authenticated():


	# 	context_data = {
	# 		"title": "My User List"

	# 	}

	# else:

	# 	context_data = {

	# 		"title": "Not a User List"


	# 	}




