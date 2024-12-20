from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import Store
from myauth.models import User, AjegUser


class CreateUserForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=[("traveller", "Traveller"), ("merchant", "Merchant")],
        widget=forms.RadioSelect,
        required=True,
    )
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["user_type", "username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        if commit:
            user.save()
        AjegUser.objects.create(
            ajeg_user=user, user_type=self.cleaned_data["user_type"]
        )
        return user


class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["name", "url", "price_range", "rating", "category"]

    def save(self, commit=True):
        store = super(CreateStoreForm, self).save(commit=False)
        if commit:
            store.save()
        ajeg_user = self.instance.ajeg_user
        ajeg_user.store.add(store)
        return store
