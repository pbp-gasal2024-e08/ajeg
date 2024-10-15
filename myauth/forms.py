from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import Toko
from myauth.models import User, AjegUser

class CreateUserForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=[('traveller', 'Traveller'), ('merchant', 'Merchant')],
        widget=forms.RadioSelect,
        required=True
        )
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [ 'user_type', 'username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        if commit:
            user.save()
        AjegUser.objects.create(
            ajeg_user=user, 
            user_type=self.cleaned_data['user_type']
            )
        return user
    
class CreateTokoForm(forms.ModelForm):
    class Meta:
        model = Toko
        fields = ['nama_toko', 'url', 'range_harga', 'rating', 'kategori']
    def save(self, commit=True):
        toko = super(CreateTokoForm, self).save(commit=False)
        if commit:
            toko.save()
        ajeg_user = self.instance.ajeg_user
        ajeg_user.toko.add(toko)
        return toko