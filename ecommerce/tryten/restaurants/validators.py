from django.core.exceptions import ValidationError
def validate_email(value):
	email=value
	if ".edu" in email:
		raise ValidationError("We don't accept edu emails")

CATEGORIES=["Mexican","Asian","American","Whatever"]

def validate_category(value):
	cat=value.capitalize()
	print cat
	if not value in CATEGORIES and not cat in CATEGORIES:
		raise ValidationError("{value} is not a valid category")