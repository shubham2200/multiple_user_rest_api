from rest_framework.permissions import BasePermission

class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_manager
        # return False

    


class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
       