from django import forms

class LoginForm(forms.Form):
	user = forms.CharField(
			label = '',
			widget = forms.TextInput(
					attrs = {
						'placeholder' : 'Enter username'
					}
				)
	)

	password = forms.CharField(
			label = '',
			widget = forms.TextInput(
					attrs = {
						'placeholder' : 'Enter password'
					}
				)
	)