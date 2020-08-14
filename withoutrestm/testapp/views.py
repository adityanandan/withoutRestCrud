from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from testapp.mixins import SerializeMixin

from testapp.utils import is_json
from testapp.forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(SerializeMixin,View):

    def get_by_object_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp

    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'please send valid json data'})
            return HttpResponse(json_data,content_type='application/json')
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_by_object_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'the Matched resource not found'})
                return HttpResponse(json_data,content_type='application/json')
            json_data=self.serialize([emp,])
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')



    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'please send valid json data'})
            return HttpResponse(json_data,content_type='application/json')
        empdata=json.loads(data)
        form=EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'data saved in database'})
            return HttpResponse(json_data,content_type='application/json')
        if form.errors:
            json_data=json.dumps(form.errors)
            return HttpResponse(json_data,content_type='application/json')



    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'please send valid json data'})
            return HttpResponse(json_data,content_type='application/json')
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'to perform update id is required'})
            return HttpResponse(json_data,content_type='application/json')
        emp=self.get_by_object_id(id)
        if emp is None:
            json_data=json.dumps({'msg':'the Matched resource not found'})
            return HttpResponse(json_data,content_type='application/json')
        provided_data=json.loads(data)
        original_data={
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eaddr':emp.eaddr,
        }
        original_data.update(provided_data)
        form=EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'data saved in database'})
            return HttpResponse(json_data,content_type='application/json')
        if form.errors:
            json_data=json.dumps(form.errors)
            return HttpResponse(json_data,content_type='application/json')



    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'please send valid json data'})
            return HttpResponse(json_data,content_type='application/json')
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_by_object_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'the Matched resource not found'})
                return HttpResponse(json_data,content_type='application/json')
            status,deleted_item=emp.delete()
            if status==1:
                json_data=json.dumps({'msg':'the resource is deleted'})
                return HttpResponse(json_data,content_type='application/json')
            json_data=json.dumps({'msg':'try again..unable to delete'})
            return HttpResponse(json_data,content_type='application/json')
        json_data=json.dumps({'msg':'to perform deletion id is mandatory'})
        return HttpResponse(json_data,content_type='application/json')




# crud opertation with different end point(argument 'id' is used)

# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeDetailCBV(View):
#     def get_by_object_id(self,id):
#         try:
#             emp=Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             emp=None
#         return emp
#
#     def get(self,request,id,*args,**kwargs):
#         try:
#             emp=Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             json_data=json.dumps({'msg':'the reqested resource not available'})
#
#         #emp_data={
#         #'eno':emp.eno,
#         #'ename':emp.ename,
#         #'esal':emp.esal,
#         #'eaddr':emp.eaddr,
#         #}
#         #json_data=json.dumps(emp_data)
#         else:
#             json_data=serialize('json',[emp,],fields=('eno','ename','eaddr'))
#         return HttpResponse(json_data,content_type='application/json')
#
#
#
#     def put(self,request,id,*args,**kwargs):
#         emp=self.get_by_object_id(id)
#         if emp is None:
#             json_data=json.dumps({'msg':'the Matched resource not found'})
#             return HttpResponse(json_data,content_type='application/json')
#         data=request.body
#         valid_json=is_json(data)
#         if not valid_json:
#             json_data=json.dumps({'msg':'please send valid json data'})
#             return HttpResponse(json_data,content_type='application/json')
#         provided_data=json.loads(data)
#         original_data={
#         'eno':emp.eno,
#         'ename':emp.ename,
#         'esal':emp.esal,
#         'eaddr':emp.eaddr,
#         }
#         original_data.update(provided_data)
#         form=EmployeeForm(original_data,instance=emp)
#         if form.is_valid():
#             form.save(commit=True)
#             json_data=json.dumps({'msg':'data saved in database'})
#             return HttpResponse(json_data,content_type='application/json')
#         if form.errors:
#             json_data=json.dumps(form.errors)
#             return HttpResponse(json_data,content_type='application/json')
#
#
#     def delete(self,request,id,*args,**kwargs):
#         emp=self.get_by_object_id(id)
#         if emp is None:
#             json_data=json.dumps({'msg':'the Matched resource not found'})
#             return HttpResponse(json_data,content_type='application/json')
#         status,deleted_item=emp.delete()
#         if status==1:
#             json_data=json.dumps({'msg':'the resource is deleted'})
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=json.dumps({'msg':'try again..unable to delete'})
#         return HttpResponse(json_data,content_type='application/json')
#








# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeelistCBV(SerializeMixin,View):
#
#     def get(self,request,*args,**kwargs):
#         qs=Employee.objects.all()
#         json_data=self.serialize(qs)
#         return HttpResponse(json_data,content_type='application/json')
#
#
#     def post(self,request,*args,**kwargs):
#         data=request.body
#         valid_json=is_json(data)
#         if not valid_json:
#             json_data=json.dumps({'msg':'please send valid json data'})
#             return HttpResponse(json_data,content_type='application/json')
#         empdata=json.loads(data)
#         form=EmployeeForm(empdata)
#         if form.is_valid():
#             form.save(commit=True)
#             json_data=json.dumps({'msg':'data saved in database'})
#             return HttpResponse(json_data,content_type='application/json')
#         if form.errors:
#             json_data=json.dumps(form.errors)
#             return HttpResponse(json_data,content_type='application/json')
