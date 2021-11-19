from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from Document.models import DocumentModel, CargoShip, Cargo
from Document.serializers import DocumentSerializer, CargoShipSerializer, CargoSerializer


class DocumentAPI(ListAPIView):
    serializer_class = DocumentSerializer
    def get_queryset(self):
        qs=DocumentModel.objects.filter()
        return qs
    def post(self,request):
        name=self.request.POST("name","")
        documents=DocumentModel.objects.all()
        cap=len(documents)
        if cap>10:
            return Response({
                "Status":False,
                "Message":"you can not add more than 10 records"
            })
        if name:
            obj=DocumentModel(name=name)
            obj.save()
            return Response({
                "Status":True,
                "Data":DocumentSerializer(obj).data,
                "Total_capacity":10,
                "Seat Left":10-cap
            })

class SymbolicAPI(ListAPIView):
    def get(self,request):
        code=self.request.GET.get("code","")
        if code:
            sum=0
            count=0
            str1=""
            for x in code:
                count = count + 1
                if (count%3)!=0:
                    if x=="r":
                        sum=sum+4;
                    elif x=="w":
                        sum=sum+2
                    elif(x=="x"):
                        sum=sum+1
                    elif(x=="-"):
                        sum=sum+0
                    else:
                        return Response({
                            "Status":False,
                            "Message":"Please choose correct string"
                        })
                    print(sum)
                elif (count%3)==0:
                    if x=="r":
                        sum=sum+4;
                    elif x=="w":
                        sum=sum+2
                    elif(x=="x"):
                        sum=sum+1
                    elif(x=="-"):
                        sum=sum+0
                    else:
                        return Response({
                            "Status":False,
                            "Message":"Please choose correct string"
                        })
                    print(count,sum)



                    print(type(sum),sum)
                    str1=str1+""+str(sum)



            return Response({
                "Status":True,
                "Decoded_Result":str1
            })
        else:
            return Response({
                "Status": False,
                "Decoded_Result": "please add a code"
            })

class CropRatio(ListAPIView):
    def get(self,request):

        return


class CargoShipAPI(ListAPIView):
    serializer_class =CargoShipSerializer
    def get_queryset(self):
        qs=CargoShip.objects.all()
        return qs
    def post(self,request):
        name=self.request.POST.get("name","")
        capacity=self.request.POST.get("capacity","")
        if name!="" and capacity!="":
            obj=CargoShip(name=name,capacity=capacity)
            obj.save()
            return Response({
                "Status":True,
                "id":obj.id,
                "name":obj.name,
                "capacity":obj.capacity
            })
        else:
            return Response({
                "Status":False,
                "Message":"provide data"
            })
class CargoAPI(ListAPIView):
    serializer_class = CargoSerializer

    def get_queryset(self):
        qs=Cargo.objects.all()
        return qs

    def post(self,request):
        name = self.request.POST.get("name", "")
        capacity = self.request.POST.get("capacity", "")
        cargoship=self.request.POST.get("cargoship","")
        print(cargoship)
        if name != "" and capacity != "" and cargoship!="":
            if cargoship:
                cs=CargoShip.objects.filter(id=cargoship).first()
                cargos=Cargo.objects.filter(CargoShip=cs)
                print(cs,cargos,cs.capacity,)
                # print(len(cs))
                if len(cargos)<cs.capacity:
                    obj = Cargo(name=name, unit=capacity,CargoShip=cs)
                    obj.save()
                    return Response({
                        "Status": True,
                        "id": obj.id,
                        "name": obj.name,
                        "capacity": obj.unit
                    })
                else:
                    return Response({
                        "Status":False,
                        "Message":"Limit exceeded"
                    })
        else:
            return Response({
                "Status": False,
                "Message": "provide data"
            })

    def delete(self,obj):
        id=self.request.GET.get("id","")
        if id:
            obj=Cargo.objects.get(id=id)
            if obj:
                obj.delete()
                return Response({
                    "Status":True,
                    "Message":"Deleted successfully"
                })
            else:
                return Response({
                    "Status": False,
                    "Message": "Can not Delete"
                })
