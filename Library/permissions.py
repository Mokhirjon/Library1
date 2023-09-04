from rest_framework.permissions import BasePermission

class ReadonlyPeromissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        print('obj information:',obj.user,obj.Library_id)
        print('user information"',request.user)
        return obj.user==request.user and request.user.is_authenticated
