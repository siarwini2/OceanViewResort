from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class StaffRequiredMixin(LoginRequiredMixin):
    """Any logged-in active staff or admin."""


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Admins only, e.g. room management, pricing rules, user management."""
    def test_func(self):
        return self.request.user.is_hotel_admin