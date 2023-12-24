from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages



from .models import UserProfile
from .forms import UserProfileForm, UpdateUserForm

from checkout.models import Order
# Create your views here.

class ProfileView(LoginRequiredMixin, View):
    template_name = 'profiles/profile.html'
    user_form_class = UpdateUserForm
    profile_form_class = UserProfileForm


    def get_context_data(self, **kwargs):
        """
        Retrieves context data for rendering the profile update page.
        Returns:
        - dict: A dictionary containing context data for rendering the page.
        """
        user = self.request.user
        profile = get_object_or_404(UserProfile, user=user)
        orders = profile.orders.all()
        context = {
            "user_form": kwargs.get("user_form",
                                    self.user_form_class(instance=user)),
            "profile_form": kwargs.get(
                "profile_form", self.profile_form_class(instance=profile)
            ),
            'orders': orders,
            'on_profile_page': True

        }
        return context


    def get(self, request):
        """
        Handles HTTP GET requests for rendering the profile update page.

        Returns:
        - HttpResponse: Renders the profile update page with context data.
        """
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        profile = get_object_or_404(UserProfile, user=request.user)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=profile)


        if "user_form" in request.POST:
            if user_form.is_valid():
                user_form.save()
                context["user_form"] = user_form
                messages.success(request, 'User updated successfully')
            else:
                context['user_form'] = user_form
                messages.error(request, 'Update failed. Please ensure the forms are valid.')
                return render(request, self.template_name, context)
        else:
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile updated successfully')
            else:
                messages.error(request, 'Update failed. Please ensure the forms are valid.')

        return render(request, self.template_name, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
