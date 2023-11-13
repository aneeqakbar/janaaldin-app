from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Class, ClassDateTime
from authentication.models import StaffMember
from .serializers import ClassSerializer

# Create your views here.

class ClassBookView(View):
    def get(self, request, id):
        class_ins = get_object_or_404(Class, id=id)
        staff_members = StaffMember.objects.all()
        context = {
          "class": class_ins,
          "staff_members": staff_members,
        }
        return render(request, "classes/book.html", context)

    def post(self, request, id):
        selected_time_id = request.POST.get("selected_time")
        class_ins = get_object_or_404(Class, id=id)
        selected_time = ClassDateTime.objects.get(id=selected_time_id)

        context = {
          "class": class_ins,
          "selected_time": selected_time,
        }

        return render(request, "classes/book-confirm.html", context)
        # return redirect("classes:ClassBookConfirmView")

class GetClassDataView(APIView):
    def get(self, request):
        class_id = request.GET.get("id", None)
        class_ins = get_object_or_404(Class, id=class_id)
        serializer = ClassSerializer(class_ins)
        return Response(serializer.data)

class ClassBookConfirmView(View):
    # def get(self, request):
    #     return render(request, "classes/book-confirm.html")

    def post(self, request):
        class_id = request.POST.get("class")
        selected_time_id = request.POST.get("selected_time")

        class_ins = get_object_or_404(Class, id=class_id)
        selected_time = ClassDateTime(id=selected_time_id)

        messages.success(request, "Class has been booked successfully, you will receive confirmination email shortly")
        return redirect("users:HomeView")

class GetClassScheduleView(View):
    def get(self, request):
        data = {}
        return JsonResponse(data)
