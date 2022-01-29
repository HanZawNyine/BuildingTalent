from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from social.api.serializers import SocialPostSerializer
from social.models import Post


@api_view(['GET', ])
def api_detail_social_view(request, slug="this-is-post"):
    try:
        post = Post.objects.get(slug=slug)
        print(post)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print('testing')
    if request.method == 'GET':
        serializer = SocialPostSerializer(post)
        return Response(serializer.data)
