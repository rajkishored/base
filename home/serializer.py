from rest_framework import serializers
# database inda baradunnna front end all thorsakke edun use madtivi(jason obj aagi)
from .models import Job,Employee,Employer,Address

class mytable(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'
class myemployee(serializers.ModelSerializer):
    class Meta:        
        model=Employee
        fields='__all__'
class myemployer(serializers.ModelSerializer):
    class Meta:
        model=Employer
        fields='__all__'
class myaddress(serializers.ModelSerializer):
    class Meta:        
        model=Address
        fields='__all__'
        


