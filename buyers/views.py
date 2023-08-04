from .models import BuyerModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BuyerInsertSerializer, BuyerGetSerializer, BuyerUpdateSerializer


# Create your views here.

@api_view(["GET", "POST", "PUT", "DELETE"])
def BuyerView(request):
    try:
        if request.method == "GET":
            params = request.query_params
            if params:
                try:
                    id = params["buyerId"]
                except:
                    id = None
                if id:
                    instance = BuyerModel.objects.get(buyerId=id)
                    data = BuyerGetSerializer(instance, many=False).data
                else:
                    return Response({"detail": "Buyer Id is required for filter results", "data": None}, 400)
            else:
                instance = BuyerModel.objects.all()
                data = BuyerGetSerializer(instance, many=True).data
            return Response({"detail": "Success", "data": data})

        elif request.method == "POST":
            data = request.data
            serializer = BuyerInsertSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"detail": "Buyer added successfully", "data": None})
            else:
                return Response({"detail": serializer.errors, "data": None}, status=400)

        elif request.method == "PUT":
            params = request.query_params
            if params:
                try:
                    id = params["buyerId"]
                except:
                    id = None
                if id:
                    data = request.data
                    try:
                        instance = BuyerModel.objects.get(buyerId=id)
                        serializer = BuyerUpdateSerializer(instance=instance, data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response({"detail": "Buyer updated successfully", "data": None})
                        else:
                            return Response({"detail": serializer.errors, "data": None}, status=400)
                    except:
                        return Response({"detail": "Record not exits to update", "data": None},
                                        status=400)
                else:
                    return Response({"detail": "Buyer Id is required to update record", "data": None}, status=400)
            else:
                return Response({"detail": "Buyer Id is required to update record", "data": None}, status=400)
        elif request.method == "DELETE":
            params = request.query_params
            if params:
                try:
                    id = params["buyerId"]
                except:
                    id = None
                if id:
                    try:
                        instance = BuyerModel.objects.get(buyerId=id)
                        instance.delete()
                        return Response({"detail": "Buyer deleted successfully", "data": None})
                    except:
                        return Response({"detail": "Record not exits to delete", "data": None},
                                        status=400)
                else:
                    return Response({"detail": "Buyer Id is required to delete record", "data": None}, status=400)
            else:
                return Response({"detail": "Buyer Id is required to delete record", "data": None}, status=400)

    except Exception as error:
        return Response({"detail": str(error)}, status=400)


@api_view(["POST"])
def BuyerSignUp(request):
    try:
        if request.method == "POST":
            data = request.data
            serializer = BuyerInsertSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"detail": "Buyer registered successfully", "data": None})
            else:
                return Response({"detail": serializer.errors, "data": None}, status=400)


    except Exception as error:
        return Response({"detail": str(error)}, status=400)


@api_view(["POST"])
def BuyerSignIn(request):
    try:
        if request.method == "POST":
            data = request.data
            try:
                instance = BuyerModel.objects.get(buyerEmailId=data["emailId"], buyerPassword=data["password"])
                if instance:
                    return Response({"detail": "Buyer Signed In successfully", "data": None})
                else:
                    return Response({"detail": "Invalid Email ID or Password", "data": None}, status=400)
            except:
                return Response({"detail": "Invalid Email ID or Password", "data": None}, status=400)


    except Exception as error:
        return Response({"detail": str(error)}, status=400)
