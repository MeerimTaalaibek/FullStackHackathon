from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsAuthorMoviePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and str(obj.author).lower() == str(request.user.email).lower())

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
