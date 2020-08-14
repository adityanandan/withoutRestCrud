from django.core.serializers import serialize
import json

class SerializeMixin(object):
    def serialize(self,qs):
        json_data=serialize('json',qs)
        p_data=json.loads(json_data)
        final=[]
        for obj in p_data:
            emp_data=obj['fields']
            final.append(emp_data)
        json_data=json.dumps(final)
        return json_data
