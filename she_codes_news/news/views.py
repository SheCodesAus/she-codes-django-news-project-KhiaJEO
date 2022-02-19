from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.views.generic.edit import DeleteView, UpdateView


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditStoryView(UpdateView):
    model = NewsStory
    template = 'news/newsstory_form.html'
    fields = ['title', 'pub_date', 'content']
    success_url = reverse_lazy('news:index')

class DeleteStoryView(DeleteView):
    model = NewsStory
    success_url = reverse_lazy('news:index')
    
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


