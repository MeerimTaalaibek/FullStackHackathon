from rest_framework.permissions import BasePermission


class IsAuthorMoviePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and str(obj.author).lower() == str(request.user.email).lower())


class IsAuthorReviewPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and str(obj.user).lower() == str(request.user.email).lower())


#
class IsProducerPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.profile_designer:
                return bool(request.user.is_authenticated)
        except:
            return False


class IsCustomerPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.profile_customer:
                return bool(request.user.is_authenticated)
        except:
            return False
