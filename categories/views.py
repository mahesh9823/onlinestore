from .models import CategoryModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CategoryInsertSerializer, CategoryGetSerializer, CategoryUpdateSerializer


# Create your views here.

@api_view(["GET", "POST", "PUT", "DELETE"])
def CategoryView(request):
    try:
        if request.method == "GET":
            params = request.query_params
            if params:
                try:
                    id = params["categoryId"]
                except:
                    id = None
                if id:
                    instance = CategoryModel.objects.get(categoryId=id)
                    data = CategoryGetSerializer(instance, many=False).data
                else:
                    return Response({"detail": "Category Id is required for filter results", "data": None}, 400)
            else:
                instance = CategoryModel.objects.all()
                data = CategoryGetSerializer(instance, many=True).data
            return Response({"detail": "Success", "data": data})

        elif request.method == "POST":
            data = request.data
            serializer = CategoryInsertSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"detail": "Category added successfully", "data": None})
            else:
                return Response({"detail": serializer.errors, "data": None}, status=400)

        elif request.method == "PUT":
            params = request.query_params
            if params:
                try:
                    id = params["categoryId"]
                except:
                    id = None
                if id:
                    data = request.data
                    try:
                        instance = CategoryModel.objects.get(categoryId=id)
                        serializer = CategoryUpdateSerializer(instance=instance, data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response({"detail": "Category updated successfully", "data": None})
                        else:
                            return Response({"detail": serializer.errors, "data": None}, status=400)
                    except:
                        return Response({"detail": "Record not exits to update", "data": None},
                                        status=400)
                else:
                    return Response({"detail": "Category Id is required to update record", "data": None}, status=400)
            else:
                return Response({"detail": "Category Id is required to update record", "data": None}, status=400)
        elif request.method == "DELETE":
            params = request.query_params
            if params:
                try:
                    id = params["categoryId"]
                except:
                    id = None
                if id:
                    try:
                        instance = CategoryModel.objects.get(categoryId=id)
                        instance.delete()
                        return Response({"detail": "Category deleted successfully", "data": None})
                    except:
                        return Response({"detail": "Record not exits to delete", "data": None},
                                        status=400)
                else:
                    return Response({"detail": "Category Id is required to delete record", "data": None}, status=400)
            else:
                return Response({"detail": "Category Id is required to delete record", "data": None}, status=400)

    except Exception as error:
        return Response({"detail": str(error)}, status=400)
