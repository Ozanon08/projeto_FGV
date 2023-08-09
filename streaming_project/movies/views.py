from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponse
from .models import Movie
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .forms import MovieForm
from django.contrib.auth import logout

#VIEWS

class MovieListView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movie_list.html', {'movies': movies})
    
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

class MovieDetailView(View):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        return render(request, 'movies/movie_detail.html', {'movie': movie})
    
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'trailer_url']
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['title', 'trailer_url']
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


def remove_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.delete()
    return redirect('movies:movie_list')

#LOGIN

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:movie_detail', movie_id=movie.pk)
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/edit_movie.html', {'form': form, 'movie': movie})


#FAVORITO

@login_required
def favorite_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        if movie in request.user.favorite_movies.all():
            request.user.favorite_movies.remove(movie)
        else:
            request.user.favorite_movies.add(movie)
        return JsonResponse({'status': 'success'})

    return redirect('movies:movie_detail', pk=pk)



#MARCAR COM ASSISTIDO
@login_required
def mark_watched(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    if movie in user.watched_movies.all():
        user.watched_movies.remove(movie)
        watched = False
    else:
        user.watched_movies.add(movie)
        watched = True

    return JsonResponse({"status": "success", "watched": watched})



