import tkinter as tk
from tkinter import *
from tkinter import ttk
import json
from walmartmodule import walmartaccountgen1

root = tk.Tk()

root.title('WalmartAccountGen')

canvas1 = tk.Canvas(root, width=1800, height=800)
canvas1.pack()

catchall = tk.Entry(root)
canvas1.create_window(200, 140, window=catchall)
password = tk.Entry(root)
canvas1.create_window(350, 140, window=password)
address = tk.Entry(root)
canvas1.create_window(500, 140, window=address)
city = tk.Entry(root)
canvas1.create_window(650, 140, window=city)
postalcode = tk.Entry(root)
canvas1.create_window(800, 140, window=postalcode)
CCnumber = tk.Entry(root)
canvas1.create_window(950, 140, window=CCnumber)
CVV = tk.Entry(root)
canvas1.create_window(1100, 140, window=CVV)
expirymonth = tk.Entry(root)
canvas1.create_window(1250, 140, window=expirymonth)
expiryYear = tk.Entry(root)
canvas1.create_window(1400, 140, window=expiryYear)
province = tk.Entry(root)
canvas1.create_window(1550, 140, window=province)
accounts = tk.Entry(root)
canvas1.create_window(1700, 140, window=accounts)

def optionsupdates():
    with open('C:/Users/andre/PycharmProjects/walmartAccountGen/options/walmartGenOptions.json', 'r+') as f:
        #x1 = catchall.get()
        #x2 = password.get()
        #x3 = address.get()
        #x4 = city.get()
        #x5 = postalcode.get()
        #x6 = CCnumber.get()
        #x7 = CVV.get()
        #x8 = expirymonth.get()
        #x9 = expiryYear.get()
        #x10 = province.get()
        #x11 = accounts.get()
        data = json.load(f)
        if catchall.get() != "":
            x1 = catchall.get()
            data['catchall'] = x1
        else:
            print("no change")
        if password.get() != "":
            x2 = password.get()
            data['password'] = x2
        else:
            print("no change")
        if address.get() != "":
            x3 = address.get()
            data['address'] = x3
        else:
            print("no change")
        if city.get() != "":
            x4 = city.get()
            data['city'] = x4
        else:
            print("no change")
        if postalcode.get() != "":
            x5 = password.get()
            data['postalcode'] = x5
        else:
            print("no change")
        if CCnumber.get() != "":
            x6 = CCnumber.get()
            data['CCnumber'] = x6
        else:
            print("no change")
        if CVV.get() != "":
            x7 = CVV.get()
            data['CVV'] = x7
        else:
            print("no change")
        if expirymonth.get() != "":
            x8 = expirymonth.get()
            data['expiryMonth'] = x8
        else:
            print("no change")
        if expiryYear.get() != "":
            x9 = expiryYear.get()
            data['expiryYear'] = x9
        else:
            print("no change")
        if province.get() != "":
            x10 = province.get()
            data['province'] = x10
        else:
            print("no change")
        if accounts.get() != "":
            x11 = accounts.get()
            data['accounts'] = x11
        else:
            print("no change")
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        f.close()

label1 = tk.Label(text="Enter Catchall")
canvas1.create_window(200, 180, window=label1)
label2 = tk.Label(text="Enter Password")
canvas1.create_window(350, 180, window=label2)
label3 = tk.Label(text="Enter Address")
canvas1.create_window(500, 180, window=label3)
label4 = tk.Label(text="Enter City")
canvas1.create_window(650, 180, window=label4)
label5 = tk.Label(text="Enter Postal Code")
canvas1.create_window(800, 180, window=label5)
label6 = tk.Label(text="Enter CCnumber")
canvas1.create_window(950, 180, window=label6)
label7 = tk.Label(text="Enter CVV")
canvas1.create_window(1100, 180, window=label7)
label8 = tk.Label(text="Enter Expiry Month (MM)")
canvas1.create_window(1250, 180, window=label8)
label9 = tk.Label(text="Enter Expiry Year (YYYY)")
canvas1.create_window(1400, 180, window=label9)
label10 = tk.Label(text="Enter Province (ON)")
canvas1.create_window(1550, 180, window=label10)
label11 = tk.Label(text="Enter Accounts")
canvas1.create_window(1700, 180, window=label11)


button1 = tk.Button(text="Save Settings", command=optionsupdates)
canvas1.create_window(950, 230, window=button1)

button2 = tk.Button(text="Start Genning Accounts", command=walmartaccountgen1.walmartgen)
canvas1.create_window(950, 270, window=button2)

root.mainloop()