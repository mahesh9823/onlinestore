from .models import SellerModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SellerInsertSerializer, SellerGetSerializer, SellerUpdateSerializer


# Create your views here.

@api_view(["GET", "POST", "PUT", "DELETE"])
def SellerView(request):
    try:
        if request.method == "GET":
            params = request.query_params
            if params:
                try:
                    id = params["sellerId"]
                except:
                    id = None
                if id:
                    instance = SellerModel.objects.get(sellerId=id)
                    data = SellerGetSerializer(instance, many=False).data
                else:
                    return Response({"detail": "Seller Id is required for filter results", "data": None}, 400)
            else:
                instance = SellerModel.objects.all()
                data = SellerGetSerializer(instance, many=True).data
            return Response({"detail": "Success", "data": data})

        elif request.method == "POST":
            data = request.data
            serializer = SellerInsertSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"detail": "Seller added successfully", "data": None})
            else:
                return Response({"detail": serializer.errors, "data": None}, status=400)

        elif request.method == "PUT":
            params = request.query_params
            if params:
                try:
                    id = params["sellerId"]
                except:
                    id = None
                if id:
                    data = request.data
                    try:
                        instance = SellerModel.objects.get(sellerId=id)
                        serializer = SellerUpdateSerializer(instance=instance, data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response({"detail": "Seller updated successfully", "data": None})
                        else:
                            return Response({"detail": serializer.errors, "data": None}, status=400)
                    except:
                        return Response({"detail": "Record not exits to update", "data": None},
                                        status=400)
                else:
                    return Response({"detail": "Seller Id is required to update record", "data": None}, status=400)
            else:
                return Response({"detail": "Seller Id is required to update record", "data": None}, status=400)
        elif request.method == "DELETE":
            params = request.query_params
            if params:
                try:
                    id = params["sellerId"]
                except:
                    id = None
                if id:
                    try:
                        instance = SellerModel.objects.get(sellerId=id)
                        instance.delete()
                        return Response({"detail": "Seller deleted successfully", "data": None})
                    except:
                        return Response({"detail": "Record not exits to delete", "data": None},
                                        status=400)
                else:
                    return Response({"detail": "Seller Id is required to delete record", "data": None}, status=400)
            else:
                return Response({"detail": "Seller Id is required to delete record", "data": None}, status=400)

    except Exception as error:
        return Response({"detail": str(error)}, status=400)


@api_view(["POST"])
def SellerSignUp(request):
    try:
        if request.method == "POST":
            data = request.data
            serializer = SellerInsertSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"detail": "Seller Registered successfully", "data": None})
            else:
                return Response({"detail": serializer.errors, "data": None}, status=400)


    except Exception as error:
        return Response({"detail": str(error)}, status=400)


@api_view(["POST"])
def SellerSignIn(request):
    try:
        if request.method == "POST":
            data = request.data
            try:
                instance = SellerModel.objects.get(sellerEmailId=data["emailId"], sellerPassword=data["password"])
                if instance:
                    return Response({"detail": "Seller Signed In successfully", "data": None})
                else:
                    return Response({"detail": "Invalid Email ID or Password", "data": None}, status=400)
            except:
                return Response({"detail": "Invalid Email ID or Password", "data": None}, status=400)


    except Exception as error:
        return Response({"detail": str(error)}, status=400)
