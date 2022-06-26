from django import forms
from django.utils.translation import ugettext_lazy as _
from male.models import MaleBlogComment



class MaleBlogCommentForm(forms.ModelForm):
    class Meta:
        model = MaleBlogComment
        fields = ('name', 'email', 'comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['name'].widget.attrs.update({'placeholder': _("Name")})
        self.fields['email'].widget.attrs.update({'placeholder': _("Email")})
        self.fields['comment'].widget.attrs.update({'placeholder': _("Type your comments..")})
