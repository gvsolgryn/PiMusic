from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    username = forms.CharField(label='닉네임(ID)', widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': '닉네임(ID) 입력'}))
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 입력'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("아이디 혹은 비밀번호가 틀립니다.")
            if not user.check_password(password):
                raise forms.ValidationError("아이디 혹은 비밀번호가 틀립니다.")
            if not user.is_active:
                raise forms.ValidationError("아이디가 활성화 되지 않았습니다. 관리자에게 문의하세요.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='닉네임(ID)', widget=forms.TextInput(attrs={'placeholder': '닉네임(ID) 입력'}))
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 입력'}))
    password2 = forms.CharField(
        label='비밀번호 재 입력',
        help_text='위와 같은 비밀번호를 다시 한번 입력해주세요.',
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 재 입력'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user
