from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import PersonForm, ExperienceForm, JustificationForm, InfoPersForm
from .models import Person , Experience, Justification, InfoPers
from .serializers import PersonSerializer, InfoPersSerializer, JustificationSerializer, ExperienceSerializer
from rest_framework import generics, status
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest


# Create your views here.



def indexView (request):
    return render(request, 'index.html')

@login_required
def dashboardView (request):
    return render(request, 'dashboard.html')

def registerView (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'Register.html', {'form': form})

def PersonFormulaire(request):
    return render(request, 'PersonsFormulaire.html')

def PortfolioAffiche (request):
    return render (request , 'portfolio.html')

def UserFormulaire (request):
    return  render(request, 'UserFormulaire.html')


def JustificationAffiche(request):
    justifications = Justification.objects.all()
    return render(request, 'JustificationAffiche.html', {'justifications': justifications})

def UserAffiche (request):
    informations = InfoPers.objects.all()
    return render(request, 'UserAffiche.html', {'informations': informations})


def ExperienceAffiche(request):
    experiences = Experience.objects.all()
    return render(request, 'ExperienceAffiche.html', {'experiences': experiences})

def PersonAdd(request):
    if request.method == 'POST':
        form = PersonForm(request.POST).save()
        return redirect('/Entities/List', {'persons', Person.objects.all()})
    else:
        form = PersonForm()
        return render(request, 'PersonsFormulaire.html', {'form': form})


def UserCoord (request):
    if request.method == 'POST':
         form = InfoPersForm(request.POST).save()
         return render(request, 'UserFormulaire.html', {'form': form} )
    else:
        form = InfoPersForm()
        return render(request, 'UserFormulaire.html', {'form': form})

def UserUpdate (request, pk):
    info = InfoPers.objects.get(id=pk)
    form = InfoPersForm()
    if request.method == "POST":
        form = InfoPers(request.POST, instance = info)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'UserFormulaire.html',context)
def UserExperience (request):
    if request.method == 'POST':
         form = ExperienceForm(request.POST).save()
         return render( request , 'ExperienceFormulaire.html', {'form': form} )
    else:
        form = ExperienceForm()
        return render(request, 'ExperienceFormulaire.html', {'form': form})

def UserJustification (request):
    if request.method == 'POST':
         form = JustificationForm(request.POST).save()
         return render(request, 'JustificationFormulaire.html', {'form': form} )
    else:
        form = JustificationForm()
        return render(request, 'JustificationFormulaire.html', {'form': form})


def PersonsView(request):
    form = PersonForm()
    return render(request, 'templates/PersonsFormulaire.html', {'form':form})

#Person GET/ POST / DELETE

@api_view(['GET'])
def get_all_Person(request):
    if request.method == 'GET':
        person=Person.objects.all()  #get all  person from the database
        if not person:  #or if len(person) ==0 or if bool(person): #if there is no person in the list
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer=PersonSerializer(person, many=True) #convert person objects to json
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message":"The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_person(request):
    if request.method == 'POST':
        person = PersonSerializer(data=request.data)  # get the person object from the request after deserialization
        if person.is_valid():  # check if the person object is valid (all required fields are filled and fields data types and format are correct)
            person.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(person.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_person(request, id):
    if request.method == 'DELETE':
        try:
            person = Person.objects.get(pk=id)
            person.delete()
            return JsonResponse({"message": "the user has been successfuly removed."},
                                status=status.HTTP_202_ACCEPTED)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def retreive_update_or_delete_Person(request, id):
    try:
        person = Person.objects.get(pk=id)
        if request.method == 'GET':

            serializer = PersonSerializer(person)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = PersonSerializer(person, data=request.data)  # get person from the request and update the instance of Person geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            person.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted person no longer exists
            # or
            # return JsonResponse({"message":"The user was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

#Experience GET/ POST/ DELETE

@api_view(['GET'])
def get_all_Exp(request):
    if request.method == 'GET':
        experience= Experience.objects.all()  #get all  experience from the database
        if not experience:  #or if len(experience) ==0 or if bool(experience): #if there is no experience in the list
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer= ExperienceSerializer(experience, many=True) #convert experience objects to json
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message":"The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_Exp(request):
    if request.method == 'POST':
        experience = ExperienceSerializer(data=request.data)  # get the experience object from the request after deserialization
        if experience.is_valid():  # check if the experience object is valid (all required fields are filled and fields data types and format are correct)
            experience.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(experience.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_Exp(request, id):
    if request.method == 'DELETE':
        try:
            experience = Experience.objects.get(pk=id)
            experience.delete()
            return JsonResponse({"message": "the experience has been successfuly removed."},
                                status=status.HTTP_202_ACCEPTED)
        except Experience.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def delete_Exp(request, id):
    if request.method == 'DELETE':
        try:
            experience = Experience.objects.get(pk=id)
            experience.delete()
            return JsonResponse({"message": "the experience has been successfuly removed."},
                                status=status.HTTP_202_ACCEPTED)
        except Experience.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def UpdateExperience (request,id):
    if request.method == 'PUT':
        try:
            experience = Experience.objects.get(pk=id) # get experience from the request and update the instance of Experience geted by nid from the DB.
            serialzer = ExperienceSerializer(experience, data=request.data)
            if serialzer.is_valid():
               serialzer.save()
               return Response(status=status.HTTP_202_ACCEPTED)

        except Experience.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET', 'PUT', 'DELETE'])
def retreive_update_or_delete_Experience(request, id):
    try:
        experience = Experience.objects.get(pk=id)
        if request.method == 'GET':

            serializer = ExperienceSerializer(experience)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = ExperienceSerializer(experience, data=request.data)  # get experience from the request and update the instance of Experience geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            experience.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted experience no longer exists
            # or
            # return JsonResponse({"message":"The experience was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# Justification GET/ POST /DELETE

@api_view(['GET'])
def get_all_Just(request):
    if request.method == 'GET':
        justification = Justification.objects.all()  #get all  justification from the database
        if not justification:  #or if len(justification) ==0 or if bool(justification): #if there is no experience in the list
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer= JustificationSerializer(justification, many=True) #convert justification objects to json
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message":"The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_just(request):
    if request.method == 'POST':
        justification = JustificationSerializer(data=request.data)  # get the justification object from the request after deserialization
        if justification.is_valid():  # check if the justification object is valid (all required fields are filled and fields data types and format are correct)
            justification.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(justification.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_just(request, id):
    if request.method == 'DELETE':
        try:
            justification = Justification.objects.get(pk=id)
            justification.delete()
            return JsonResponse({"message": "the justification has been successfuly removed."},
                                status=status.HTTP_202_ACCEPTED)
        except Justification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PUT', 'DELETE'])
def retreive_update_or_delete_Justification(request, id):
    try:
        justification = Justification.objects.get(pk=id)
        if request.method == 'GET':

            serializer = JustificationSerializer(justification)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = JustificationSerializer(justification, data=request.data)  # get justification from the request and update the instance of Justification geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            Justification.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted justification no longer exists

        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

#InfoPers GET/ POST / DELETE / RUP

@api_view(['GET'])
def get_all_InfoPers(request):
    if request.method == 'GET':
        informations = InfoPers.objects.all()  #get all  informations from the database
        if not informations:  #or if len(informations) ==0 or if bool(justification): #if there is no experience in the list
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer= InfoPersSerializer(informations, many=True) #convert informations objects to json
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message":"The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_InfoPers(request):
    if request.method == 'POST':
        information = InfoPersSerializer(data=request.data)  # get the info object from the request after deserialization
        if information.is_valid():  # check if the info object is valid (all required fields are filled and fields data types and format are correct)
            information.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(information.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_InfoPers(request, id):
    if request.method == 'DELETE':
        try:
            information = InfoPers.objects.get(pk=id)
            information.delete()
            return JsonResponse({"message": "the information has been successfuly removed."},
                                status=status.HTTP_202_ACCEPTED)
        except InfoPers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def UpdateInfoPers (request,id):
    if request.method == 'PUT':
        try:
            information = InfoPers.objects.get(pk=id) # get experience from the request and update the instance of Experience geted by nid from the DB.
            serialzer = InfoPersSerializer(information, data=request.data)
            if serialzer.is_valid():
               serialzer.save()
               return Response(status=status.HTTP_202_ACCEPTED)

        except InfoPers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def retreive_update_or_delete_infopers(request, id):
    try:
        informations = InfoPers.objects.get(pk=id)
        if request.method == 'GET':

            serializer = InfoPersSerializer(informations)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = InfoPersSerializer(informations,
                                        data=request.data)  # get informations from the request and update the instance of infopers geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            informations.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted informations no longer exists
            # or
            # return JsonResponse({"message":"The information was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except InfoPers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

class PersonList(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class ExperienceList(generics.ListCreateAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class JustificationList(generics.ListCreateAPIView):
    serializer_class = JustificationSerializer
    queryset = Justification.objects.all()


class JustificationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JustificationSerializer
    queryset = Justification.objects.all()


class InfoPersList(generics.ListCreateAPIView):
    serializer_class = InfoPersSerializer
    queryset = InfoPers.objects.all()


class InfoPersDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InfoPersSerializer
    queryset = InfoPers.objects.all()





