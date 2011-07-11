#coding=utf-8
from django import forms
from django.db.models import get_model
from models import *

def SerialSave(ins, data_dic):
    for k in data_dic:
        if ins.__dict__.get(k):
            ins.__dict__[k] = data_dic[k]
    return ins.save()

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=64)
    description = forms.CharField(required=False)
    class Meta:
        model = Category
        fields = ('name', 'description')

class KnowForm(forms.ModelForm):
    category = forms.CharField(max_length=9) # receive nid, return object after clean_
    name = forms.CharField(max_length=64)
    brief = forms.CharField()
    refer_object = forms.CharField(max_length=64, required=False)
    refer_md5id = forms.CharField(max_length=32, required=False)
    father_nid = forms.CharField(max_length=8, required=False) # father & son
    ##
    tags = forms.CharField(max_length=256)
    class Meta:
        model = Category
    def __init__(self, instance=None, *args, **kwargs):
        self._instance = instance
        super(KnowForm, self).__init__(*args, **kwargs)
    def clean_category(self):
        """nid -> object"""
        data = self.cleaned_data['category']
        category = Category.by_nid(data)
        if not category:
            raise ValidationError('Category Unexist')
        return category
    def clean_refer_md5id(self):
        """
        require refer_object same time
        """
        data = self.cleaned_data['refer_md5id']
        object_model = get_model(self.cleaned_data['refer_object'])
        if not object_model:
            raise forms.ValidationError("Invalid refer object")
        try:
            ins = object_model.objects.get(md5id=data)
        except:
            raise forms.ValidationError("Invalid refer md5id")
        return data
    def clean_father_nid(self):
        data = self.cleaned_data['father_nid']
        if not Knowledge.by_nid(data):
            raise forms.ValidationError('Invalid father nid')
        return data
    def cleaned_tags(self):
        """seperated by commas (both in zh & en)"""
        comma_zh = u'，'
        comma_en = ','
        tag_list = []
        loop0 = self.cleaned_data['tags']
        loop1 = loop0.split(comma_en)
        for i in loop1:
            if i.find(comma_zh):
                tag_list[len(tag_list):] = i.split(comma_zh)
            else:
                tag_list.append(i)
        print tag_list
        # check tags #
        #for i in tag_list:
    def save(self, *args, **kwargs):
        data = self.cleaned_data
        ins = self._instance
        if ins:
            return SerialSave(ins, data)
        else:
            return super(KnowForm, self).save(*args, **kwargs)
