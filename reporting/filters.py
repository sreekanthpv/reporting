import django_filters
from reporting.models import TimeSheet,Batch
from django import forms

class TimeSheetFilter(django_filters.FilterSet):

   date = django_filters.DateFilter(widget=forms.DateInput(attrs={"type":"date","class":"form-control w-50"}))
   batch=django_filters.ModelChoiceFilter(queryset=Batch.objects.all(),widget=forms.Select(attrs={"class":"form-select w-50"}))
   class Meta:

        model = TimeSheet
        # topic = django_filters.CharFilter(lookup_expr = "icontains")
        fields = ["batch","date"]
