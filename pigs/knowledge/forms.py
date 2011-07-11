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
    tags = forms.CharField(max_length=256, required=False)
    class Meta:
        model = Knowledge
        fields = ('category', 'name', 'brief', 'refer_object', 'refer_md5id', 'father_nid', 'tags')
    def clean_category(self):
        """
        nid -> object
        """
        data = self.cleaned_data.get('category')
        category = Category.by_nid(data)
        if not category:
            raise forms.ValidationError('Category Unexist')
        return category
    def clean_refer_md5id(self): # not required
        """
        require refer_object same time
        """
        data = self.cleaned_data.get('refer_md5id')
        data_object = self.cleaned_data.get('refer_object')
        if not data:
            return None
        if not data_object:
            raise forms.ValidationError('Need refer object')
        try:
            object_model = get_model(*data_object.split('.'))
        except:
            raise forms.ValidationError("Invalid refer object")
        try:
            ins = object_model.objects.get(md5id=data)
        except:
            raise forms.ValidationError("Invalid refer md5id")
        return data
    def clean_father_nid(self): # not required
        data = self.cleaned_data.get('father_nid')
        if not data:
            return None
        if not Knowledge.by_nid(data):
            raise forms.ValidationError('Invalid father nid')
        return data
    def cleaned_tags(self): # not required
        data = self.cleaned_data.get('tags')
        if not data:
            return None
        """seperated by commas (both in zh & en)"""
        comma_zh = u'，'
        comma_en = ','
        tag_list = []
        loop0 = data
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
        return super(KnowForm, self).save(*args, **kwargs)
