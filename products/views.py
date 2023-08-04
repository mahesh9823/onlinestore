from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductInsertSerializer, ProductGetSerializer, ProductUpdateSerializer
from .models import ProductModel


# Create your views here.

@api_view(["GET", "POST", "PUT", "DELETE"])
def ProductView(request):
    try:
        if request.method == "GET":
            params = request.query_params
            if params:
                try:
                    sellerId = params["sellerId"]
                except:
                    sellerId = None

                try:
                    categoryId = params["categoryId"]
                except:
                    categoryId = None

                try:
                    productId = params["productId"]
                except:
                    productId = None

                if categoryId and sellerId:
                    instance = ProductModel.objects.filter(sellerId=sellerId, categoryId=categoryId)
                    data = ProductGetSerializer(instance, many=True).data
                elif productId:
                    instance = ProductModel.objects.get(productId=productId)
                    data = ProductGetSerializer(instance, many=False).data
                elif categoryId:
                    instance = ProductModel.objects.filter(categoryId=categoryId)
                    data = ProductGetSerializer(instance, many=True).data
                elif sellerId:
                    instance = ProductModel.objects.filter(sellerId=sellerId)
                    data = ProductGetSerializer(instance, many=True).data
                else:
                    return Response({"detail": "Product Id or Category Id or Seller Id is required for filter results", "data": None},
                                    400)
            else:
                serializer = ProductModel.objects.all()

                data = ProductGetSerializer(serializer, many=True).data
            return Response({"detail": "Success", "data": data})

        elif request.method == "POST":
            data = request.data
            serializer = ProductInsertSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                return Response({"detail": "Seller added successfully", "data": None})
            else:
                return Response({"detail": serializer.errors, "data": None}, status=400)

        elif request.method == "PUT":
            params = request.query_params
            if params:
                try:
                    id = params["productId"]
                except:
                    id = None
                if id:
                    data = request.data
                    try:
                        instance = ProductModel.objects.get(productId=id)
                        serializer = ProductUpdateSerializer(instance=instance, data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response({"detail": "Product updated successfully", "data": None})
                        else:
                            return Response({"detail": serializer.errors, "data": None}, status=400)
                    except:
                        return Response({"detail": "Record not exits to update", "data": None},
                                        status=400)
                else:
                    return Response({"detail": "Product Id is required to update record", "data": None}, status=400)
            else:
                return Response({"detail": "Product Id is required to update record", "data": None}, status=400)
        elif request.method == "DELETE":
            params = request.query_params
            if params:
                try:
                    id = params["productId"]
                except:
                    id = None
                if id:
                    try:
                        instance = ProductModel.objects.get(productId=id)
                        instance.delete()
                        return Response({"detail": "Product deleted successfully", "data": None})
                    except:
                        return Response({"detail": "Record not exits to delete", "data": None},
                                        status=400)
                else:
                    return Response({"detail": "Product Id is required to delete record", "data": None}, status=400)
            else:
                return Response({"detail": "Product Id is required to delete record", "data": None}, status=400)



    except Exception as error:
        return Response({"detail": str(error)}, status=400)
