from rest_framework import permissions

class IsCreatorOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		"""
		Custom permissions that allows only the creator of a tweet to modify it
		"""
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj.creator == request.user