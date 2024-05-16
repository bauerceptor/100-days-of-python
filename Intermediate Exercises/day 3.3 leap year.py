# if year % 4 == 0:
#   print("Leap year.")
#   if year % 100 != 0:
#     print("Leap year.")
#   else:
#     print("Not leap year.")
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
# else:
#   print("Not leap year.")
  
year = int(input("Which year do you want to check? "))
if year % 4 != 0:
  print("Not leap year.")
else:
  if year % 100 !=0:
    print("Leap year.")
  else:  
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")




  
  
  