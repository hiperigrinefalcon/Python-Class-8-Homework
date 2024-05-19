filename = 'contacts.txt'

#info = {}

info_list_of_dict = []
info = {'Name':'no name','phone_num':1234567890}
info_list_of_dict.append(info)
print(info_list_of_dict)
contact_info = True
while contact_info == True:
  Name = input("Input name: ")
  phone_num = input("Input a phone number(10-11 digits): ")
  Phone_num = int(phone_num)

  
  
  info = {'Name':Name, 'phone_num':Phone_num}

  new_contact_info = True
  #print(info_list_of_dict)
  for each_piece_of_info in info_list_of_dict:
    #print("here inside for")
    print(each_piece_of_info.values())
    if Name in each_piece_of_info.values():
      #print("here22")
      #print(Name)
      print("This name is already in the list.")
      new_contact_info = False
      break
    elif Phone_num in each_piece_of_info.values():
      #print("here33")
      print("This phone number is already in the list.")
      new_contact_info = False
      break
    else:
      continue
  if new_contact_info == True:
    with open (filename, 'a') as file_object:
      file_object.write(Name + ',' + phone_num + '\n')
    print("appending to list")
    info_list_of_dict.append(info)
  input_again = input("Would you like to input more information?(answer yes or no): ")
  if input_again == "yes":
    contact_info = True
  elif input_again == "no":
    contact_info = False
  else:
    print("Invalid input.")
    contact_info = False

print(info_list_of_dict)

info_list_of_dict[0]


# with open (filename,'w') as file_object:
#  file_object.write("hello")
