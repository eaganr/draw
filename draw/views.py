import json

from django.shortcuts import render
from django.http import HttpResponse

from painting.models import Dot

def home(request):
	if request.method == "POST":
		if "xpos" in request.POST:
			xpos = int(request.POST["xpos"])
			ypos = int(request.POST["ypos"])
			color = request.POST["color"]
			d = Dot(xpos=xpos, ypos=ypos, color=color)
			d.save()
			if len(Dot.objects.all()) > 100:
				Dot.objects.all()[0].delete()
			return HttpResponse(str(d.pk))
		if request.POST.getlist("dotPks[]"):
			dots = Dot.objects.all()
			for dot in dots:
				if str(dot.pk) not in request.POST.getlist("dotPks[]"):
					new_dot = {}
					new_dot = {}
					new_dot["color"] = dot.color
					new_dot["xpos"] = int(dot.xpos)
					new_dot["ypos"] = int(dot.ypos)
					new_dot["pk"] = dot.pk
					return HttpResponse(json.dumps(new_dot), content_type="application/json")
			return HttpResponse("")

	dots = Dot.objects.all()
	context = {}
	context["dots"] = dots
	if len(dots) > 0:
		context["dotsPk"] = dots[len(dots)-1].pk
	pkList = ""
	for dot in dots:
		pkList = pkList + str(dot.pk) + ","
	context["pkList"] = pkList
	return render(request, 'draw/home.html', context)