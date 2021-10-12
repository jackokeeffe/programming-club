# Goes over .split()
# Input: frodo.baggins@ring.com
# Show username (frodo.baggins) and domain address (ring.com)

email = str(input("Enter email: "))

split_email = email.split("@")

print("Hello " + split_email[0] + "!")
print("Your email domain is " + split_email[1] + ".")