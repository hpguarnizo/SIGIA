# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.generic import TemplateView

#El RequestContext permite mantender informacion del request de la pagina que hizo la peticion 
#y pasarsela a la nueva pagina, esto eprmite mantener datos como el usuario logeado entre otros
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from apps.empleado.models import Empleado


class Login(TemplateView):

	#Cuando la peticion es tipo GET, se muestra el template de login
	def get(self,request,*args,**kwargs):
		#Si el usuario esta autenticado, se le muestra su perfil
		if request.user.is_authenticated():
			return render_to_response('cuenta/perfil.html',context_instance=RequestContext(request))
		#En caso de que no este autenticado, se le muestra el formulario de login
		else:
			return render_to_response('inicio/login.html',context_instance=RequestContext(request))
		
		

	#Cunado la peticion es tipo POST se hace el proceso de login con la informacion del formulario de login
	def post(self,request,*args,**kwargs):
		username = request.POST.get('username')
		password = request.POST.get('password')


		#Usando el la funcion authenticate, obtenemos el usuario que corresponde con los datos 
		#pasados como argumentos
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
							
				#Retornamos una respuesta con el perfil del usuario
				return render_to_response('cuenta/perfil.html',context_instance=RequestContext(request))
			else:
				context = {'message':'Su usuario no esta activo'}
				return render_to_response('inicio/login.html',context,context_instance=RequestContext(request))
		else:
			context = {'message':'Usuario o contraseña invalido'}
			return render_to_response('inicio/login.html',context,context_instance=RequestContext(request))

class Logout(TemplateView):

	def dispatch(self,request,*args,**kwargs):
		logout(request)
		context = {}
		return render_to_response('inicio/login.html',context,context_instance=RequestContext(request))

