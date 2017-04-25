from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from eventos.models import Palestra, VisitaTecnica, MiniCurso
from django.contrib.auth.decorators import login_required

# class UserProfile(generic.View):
#     model = User
#     template_name = 'profile/index.html'
#
#     def get_objects(self):
#         try:
#             return self.request.user.get_profile()
#         except ProfileDoesNotExist:
#             raise NotImplemented( "User profile page does not exist")
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(UserProfile, self).get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['all_visitas'] = self.visitatecnica_set.all()
#         context['all_minicursos'] = self.minicurso_set.all()
#         context['all_palestras'] = self.palestra_set.all()
#         return context

@login_required
def profile(request):
        user = request.user
        # try:
        #     user =  self.request.user.
        # except ProfileDoesNotExist:
        #     raise NotImplemented( "User profile page does not exist")

        context = {
        'palestras': user.profileuser.palestra_set.all(),
        'visitas': user.profileuser.visitatecnica_set.all(),
        'minicursos': user.profileuser.minicurso_set.all()
}
        return render(request, 'profile/index.html', context)
