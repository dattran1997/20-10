from models.collection import User, Present
import mlab
import xlrd
mlab.connect()

# acccountname = input("hay nhap ten acc: ")
# username = input("hay nhap ten user: ")
# password = input("hay nhap pass: ")
# image = input('hay nhap anh: ')
#
# new_user = User(acccountname = acccountname ,username = username, password = password, image = image)
# new_user.save()
# print("save successful")

# user = User.objects.get(username = "dattran")
# reciverid = str(user.id)
# sendername = input("nhap ten nguoi gui: ")
# image = input('nhap anh người gửi: ')
# wishing = input("nhap loi chuc: ")
#
# new_present = Present(reciverid = reciverid, sendername = sendername, image = image, wishing = wishing)
# new_present.save()
# print("send successful")

loc = ("20_10.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
# hà, huyền, thảo, hằng, linh
list_id =["5be0267e129995827aff0068","5be0293512999586f214b193","5be026e01299957f66440c79","5be0297d129995190ef716a1","5be0284d1299958f4a7e4e1d"]

for i in range (sheet.nrows - 1):
    list =sheet.row_values(i+1)
    for id in list_id:
        if id == list_id[0]:
            #present
            reciverid = id
            sendername = list[0]
            image = str(i+1)
            wishing = list[1]
            new_present = Present(reciverid = reciverid, sendername = sendername, image = image, wishing = wishing)
            new_present.save()
        if id == list_id[1]:
            #present
            reciverid = id
            sendername = list[0]
            image = str(i+1)
            wishing = list[2]
            new_present = Present(reciverid = reciverid, sendername = sendername, image = image, wishing = wishing)
            new_present.save()
        if id == list_id[2]:
            #present
            reciverid = id
            sendername = list[0]
            image = str(i+1)
            wishing = list[3]
            new_present = Present(reciverid = reciverid, sendername = sendername, image = image, wishing = wishing)
            new_present.save()
        if id == list_id[3]:
            #present
            reciverid = id
            sendername = list[0]
            image = str(i+1)
            wishing = list[4]
            new_present = Present(reciverid = reciverid, sendername = sendername, image = image, wishing = wishing)
            new_present.save()
        if id == list_id[4]:
            #present
            reciverid = id
            sendername = list[0]
            image = str(i+1)
            wishing = list[5]
            new_present = Present(reciverid = reciverid, sendername = sendername, image = image, wishing = wishing)
            new_present.save()
    print(list[0],"successful")
