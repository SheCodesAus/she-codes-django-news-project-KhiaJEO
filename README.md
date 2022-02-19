# Plus Resources: Django Project Starter

Starter code for the Plus Django project.

She Codes News URL:
https://stark-refuge-35528.herokuapp.com/news/

user to login with: 
username: pumpkinsoup
password: pumpkinsoup







to delete if neccesary
# for the VIEW BY AUTH
    
# class ViewByAuthorView(generic.Listview):
#         model = NewsStory
#         template_name = 'news/viewbyauthor.html'     


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
#         context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
#         return context


# View by author
# class AuthorsView(ListView):
#     # model = CustomUser
#     template_name = 'users/authors.html'
#     # context_object_name = 'authors'

#     def get_queryset(self):
#         self.authors = get_object_or_404(CustomUser, name=self.kwargs['authors'])
#         return NewsStory.objects.filter(authors=self.authors)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['authors'] = self.authors
#         return context

# path('authors/', AuthorsView.as_view(), name='authors'),