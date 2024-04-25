from rest_framework.views import APIView
from menu.models import FoodCategory
from menu.serializers import FoodSerializer, FoodListSerializer
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK)


class APIFoodList(APIView):
    """View для получения списка категорий блюд."""
    def get(self, request):
        food_categories = FoodCategory.objects.prefetch_related('food').filter(
            food__is_publish=True).distinct()
        serialized_data = []

        for category in food_categories:
            category_data = FoodListSerializer(category).data
            category_data['foods'] = FoodSerializer(
                category.food.filter(is_publish=True), many=True
                ).data
            if category_data['foods']:
                serialized_data.append(category_data)

        return Response(serialized_data[::-1], status=HTTP_200_OK)
