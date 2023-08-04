from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CartInsertSerializer, CartGetSerializer, CartUpdateSerializer
from .models import CartModel


# Create your views here.

@api_view(["GET", "POST", "PUT", "DELETE"])
def CartView(request):
    try:
        if request.method == "GET":
            params = request.query_params
            if params:
                try:
                    buyerId = params["buyerId"]
                except:
                    buyerId = None

                try:
                    cartId = params["cartId"]
                except:
                    cartId = None

                if cartId:
                    instance = CartModel.objects.get(cartId=cartId)
                    data = CartGetSerializer(instance, many=False).data
                elif buyerId:
                    instance = CartModel.objects.filter(buyerId=buyerId)
                    data = CartGetSerializer(instance, many=True).data

                else:
                    return Response({"detail": "Cart Id or Buyer Id is required for filter results", "data": None},
                                    400)
            else:
                serializer = CartModel.objects.all()

                data = CartGetSerializer(serializer, many=True).data
            return Response({"detail": "Success", "data": data})

        elif request.method == "POST":
            data = request.data
            serializer = CartInsertSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                return Response({"detail": "Product added to cart successfully", "data": None})
            else:
                return Response({"detail": serializer.errors, "data": None}, status=400)

        elif request.method == "PUT":
            params = request.query_params
            if params:
                try:
                    id = params["cartId"]
                except:
                    id = None
                if id:
                    data = request.data
                    try:
                        instance = CartModel.objects.get(cartId=id)
                        serializer = CartUpdateSerializer(instance=instance, data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response({"detail": "Products updated in Cart successfully", "data": None})
                        else:
                            return Response({"detail": serializer.errors, "data": None}, status=400)
                    except:
                        return Response({"detail": "Record not exits to update", "data": None},
                                        status=400)
                else:
                    return Response({"detail": "Cart Id is required to update record", "data": None}, status=400)
            else:
                return Response({"detail": "Cart Id is required to update record", "data": None}, status=400)
        elif request.method == "DELETE":
            params = request.query_params
            if params:
                try:
                    id = params["cartId"]
                except:
                    id = None
                if id:
                    try:
                        instance = CartModel.objects.get(cartId=id)
                        instance.delete()
                        return Response({"detail": "Products deleted from Cart successfully", "data": None})
                    except:
                        return Response({"detail": "Record not exits to delete", "data": None},
                                        status=400)
                else:
                    return Response({"detail": "Cart Id is required to delete record", "data": None}, status=400)
            else:
                return Response({"detail": "Cart Id is required to delete record", "data": None}, status=400)



    except Exception as error:
        return Response({"detail": str(error)}, status=400)
