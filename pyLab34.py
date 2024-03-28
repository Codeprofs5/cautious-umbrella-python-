# # 34.Write a program that reads email-id of a person
# # in the form of a string and ensures that it belongs
# # to domain @gce.ac.in.
# # (assume invalid characters are not there in emails)
emailID = input("Enter your email address: ")
if emailID.lower().find("@gce.ac.in") != -1 and emailID:
    print("valid email address")
else:
    print("not valid email address")



