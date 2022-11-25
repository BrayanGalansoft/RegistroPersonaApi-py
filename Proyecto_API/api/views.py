from django.views import View
from .models import Persona
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class PersonaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,id=0):
        if (id>0):
            personas=list(Persona.objects.filter(id=id).values())
            if len(personas)>0:
                persona=personas[0]
                datos={'message': 'Success','Personas':persona}
            else:
                datos={'message': 'No existe la persona..'}
            return JsonResponse(datos)
        else:
            persona=list(Persona.objects.values())
            if len(persona)>0:
                datos={'message': 'Success','Personas':persona}
            else:
                datos={'message': 'No hay personas..'}
            return JsonResponse(datos)

    def post(self,request):
        jd = json.loads(request.body)
        Persona.objects.create(nombre=jd['nombre'],apellido=jd['apellido'],correo=jd['correo'])
        datos = {'message' : 'Success'}
        return JsonResponse(datos)

    def put(self,request,id):
        jd = json.loads(request.body)
        personas=list(Persona.objects.filter(id=id).values())
        if len(personas)>0:
            persona=Persona.objects.get(id=id)
            persona.nombre = jd['nombre']
            persona.apellido = jd['apellido']
            persona.correo = jd['correo']
            persona.save()
            datos = {'message' : 'Success'}
        else:
             datos={'message': 'No existe la persona..'}
        return JsonResponse(datos)
    def delete(self,request,id):
        personas=list(Persona.objects.filter(id=id).values())
        if len(personas)>0:
            Persona.objects.filter(id=id).delete()
            datos = {'message' : 'Success'}
        else:
             datos={'message': 'No existe la persona..'}
        return JsonResponse(datos)
       