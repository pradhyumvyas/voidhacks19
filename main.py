import tkinter
from tkinter import *
from tkinter import Tk, messagebox
#from PIL import ImageTk
import mysql
import mysql.connector
import sql as sql


def logoutp():
    exit()
def tranction():
    root = Tk()
    root.title("Payment Gateway")
    root.geometry("400x400")
    # login.destroy()

    # u="hi"
    def retrieve_input():
        inputValue = textBox.get("1.0", "end-1c")
        inputValue1 = textBox1.get("1.0", "end-1c")
        x = inputValue;
        y = inputValue1;

        print(x)
        print(y)
        import hashlib

        import pymysql
        conn=mysql.connector.connect(
            host="192.168.150.68",
            user="an",
            passwd="an",
            database="employee",
            port=3306)
        connpy=mysql.connector.connect(
            host="192.168.150.70",
            user="anp",
            passwd="an",
            database="codesena",
            port=3306)

        #conn = pymysql.connect(host='192.168.150.68', port=3306, user='an', passwd='an', db='employee')
       #connpy = pymysql.connect(host='192.168.150.70', port=3306, user='anp', passwd='an', db='codesena')

        senduser = "anamika"
        # senduser=u;
        widd=x #reciver waller ID

        # widd = "2d6c9a90dd38f6852515274cde41a8cd8e7e1a7a053835334ec7e29f61b918dd"
        cu = conn.cursor()
        se = "SELECT username FROM wid WHERE wid ='" + widd + "'"
        cu.execute(se)
        j = cu.fetchall()
        for wali in j:
            wali

        walidtouser = ''.join(wali)

        recuser = walidtouser

        print(recuser)

        # recuser ="ree"
        cur_sen = conn.cursor()
        cur_rec = conn.cursor()
        # yt=''.join(senduser)
        sen_sql = "SELECT wid FROM wid WHERE username ='" +senduser+ "';"
        rec_sql = "SELECT wid FROM wid WHERE username ='" + recuser + "';"
        cur_sen.execute(sen_sql)
        cur_rec.execute(rec_sql)
        t = cur_sen.fetchall()

        q = cur_rec.fetchall()
        for row in t:
            row
        r = ''.join(row)
        # print(r+" rec")

        for ro in q:
            ro
        u = ''.join(ro)

        # ammount = 500
        ammount =y
        ammount=int(ammount)
        # query to fetch amount
        amm_sen = conn.cursor()
        amm_rec = conn.cursor()
        print(senduser)
        print("senduser")
        amsen_sql = "SELECT balance FROM wid WHERE username ='" + senduser + "'";
        amrec_sql = "SELECT balance FROM wid WHERE username ='" + recuser + "'";

        # amm_sen.execute(amsen_sql)
        amm_rec.execute(amrec_sql)
        sam = amm_sen.fetchall()
        ram = amm_rec.fetchall()
        for amrow in sam:
            amrow
        # se=amrow#''.join(amrow)
        amrow = int(amrow[0])
        print(amrow)
        print(ammount)
        print("ammouttt")
        print(amrow)
        print("amountbbbbb")
        if amrow >= ammount:
            print("Possible")
            for amro in ram:
                amro
            amro = int(amro[0])
            re = amro  # ''.join(amro)
            print(re)  # \+" Reciver amount")
            # re_am=int(re)
            # se_am=int(se)

            # print(u+" sen")

            amm = str(ammount)
            # hash cal for transaction

            th = r + u + amm
            # print(th)

            tran_hash = hashlib.sha256(th.encode()).hexdigest()
            print(tran_hash + " trchash")
            # update Balance

            up_sen = conn.cursor()
            up_sen_py = connpy.cursor()
            up_rec = conn.cursor()
            up_rec_py = connpy.cursor()
            sen_up = "UPDATE wid SET balance=balance -'" + amm + "'WHERE username='" + senduser + "'"
            rec_up = "UPDATE wid SET balance=balance +'" + amm + "'WHERE username='" + recuser + "'"
            up_sen.execute(sen_up)
            up_rec_py.execute(rec_up)
            up_sen_py.execute(sen_up)
            up_rec.execute(rec_up)
            print("sender balance update succes")
            # up_rec.execute(rec_up)
            conn.commit()
            connpy.commit()

            # t=1
            mycursor11 = conn.cursor()
            mycursor21 = connpy.cursor()
            #
            mycursor11.execute("SELECT BLOCKID FROM transaction ORDER BY Time desc LIMIT 1")

            print(mycursor11.description)
            print()

            for blockid in mycursor11:
                print(blockid)
            blockid = int(blockid[0])
            # blockid=
            print("aaaa")
            print(blockid)

            mycursor11 = conn.cursor()
            mycursor21 = connpy.cursor()

            mycursor11.execute("SELECT hash FROM transaction ORDER BY Time desc LIMIT 1;")

            print(mycursor11.description)
            print()

            for l in mycursor11:
                print(l)
            # privious_hash
            print("aabbbb")
            previous_hash = ''.join(l)
            # privious_hash=
            print(previous_hash)

            from datetime import datetime

            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
            print('Current Timestamp : ', timestampStr)
            index = blockid + 1
            index = int(index)
            print("Inndex")
            print(index)
            print(blockid)
            # previous_hash="zcwc22223"
            data = tran_hash
            k = previous_hash + data + timestampStr;

            b = hashlib.sha256(k.encode()).hexdigest()
            print(b + " blockhash")


            print("Indexx")
            print(index)


            sql = "INSERT INTO transaction (BlockId,Hash,PreviousHash,Time) VALUES (%s, %s,%s, %s)"
            val = (index, b, previous_hash, timestampStr)

            mycursor11.execute(sql, val)
            mycursor21.execute(sql, val)
            print("Aniruddh")

            conn.commit()
            connpy.commit()

            cur_rec.close()
            cur_sen.close()

            conn.close()



        else:
            messagebox.showwarning("Warning","Incefficient Balance")
            print("Not Possible")

    First_Name = tkinter.Label(root, text="Recivers Wallet ID:",fg="blue").place(x=30, y=100)
    Middle_Name = tkinter.Label(root, text="Amount:",fg="blue").place(x=30, y=150)

    textBox = Text(root, height=1, width=13)
    textBox.place(x=250, y=100)
    textBox1 = Text(root, height=1, width=13)
    textBox1.place(x=250, y=150)

    buttonCommit = Button(root, height=1, width=10, text="Pay", fg="blue",
                          command=lambda: retrieve_input())
    buttonCommit.place(x=150, y=200)

    mainloop()

# --------------------------PAYMENT PAGE_-------------------------------------



def dbs():
    top = Tk()
    top.geometry("600x400")
    top.title("Payment Page")
    l5 = Label(top, text="Receiver's Wallet ID :",fg="blue").place(x=30, y=70)
    t9=Text(top, width=30, height=1).place(x=160, y=70)
    l6=Label(top, text="Amount",fg="blue").place(x=30, y=120)
    t10=Text(top, width=30, height=1).place(x=160, y=120)

    s1=Button(top, text="SEND",fg="blue", command=tranction).place(x=70, y=150)

    top.mainloop()
#--------------------------------LOGIN BUTTON--------------------------------
def loginp():
    login.withdraw()
    inputValue10 = textBo.get("1.0", "end-1c")
    inputValue11 = textBo1.get("1.0", "end-1c")
    a = inputValue10;
    b = inputValue11;
    print(a)
    print(b)
    mydb = mysql.connector.connect(
        host="192.168.150.68",
        user="an",
        passwd="an",
        database="employee"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM userlist  where username='"+a+"'and password='"+b+"'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    #_---------------------------LOGIN AFTER PAGE---------------------------------
    if myresult :
        sql = "SELECT wid FROM wid  where username='" + a + "'"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()


        top = Tk()
        top.title("Profile")
        top.resizable(False, False)
        # root.title("Profile")
        top.geometry("600x300")
        l1 = Label(top, text="Wallet ID :",fg="blue").place(x=30, y=80)
        t1 = Label(top, text=myresult).place(x=100, y=80)
        l2 = Label(top, text="Balance :",fg="blue").place(x=30, y=130)

        sql1 = "SELECT balance FROM wid  where username='" + a + "'"
        # print(+" bal")
        mycursor.execute(sql1)

        myresult1 = mycursor.fetchall()
        # print(myresult1+" bal")
        t2 = Label(top, text=myresult1).place(x=100, y=130)
        b1 = Button(top, text="   Send   ",command=tranction,fg="blue").place(x=130, y=210)
        b1 = Button(top, text="  Logout ",command=logoutp,fg="blue").place(x=220, y=210)
        top.mainloop()

    else:
        messagebox.showinfo("Warning", "username/password may incorrect")


#----------------------------------------SIGNUP BUTTON--------------------------------------
def signup1():
    import hashlib
    import tkinter

    import mysql.connector

    login.withdraw()
    root = Tk()
    root.title("Signup")
    root.geometry("400x600")
    root.resizable(False, False)

    def retrieve_input():
        inputValue = textBox.get("1.0", "end-1c")
        inputValue1 = textBox1.get("1.0", "end-1c")
        inputValue2 = textBox2.get("1.0", "end-1c")
        inputValue3 = textBox3.get("1.0", "end-1c")
        inputValue4 = textBox4.get("1.0", "end-1c")
        inputValue5 = textBox5.get("1.0", "end-1c")
        inputValue6 = textBox6.get("1.0", "end-1c")
        # inputValue1 = textBox1.get("1.0", "end-1c")
        # print(inputValue)
        a = inputValue;
        b = inputValue1;
        c = inputValue2;
        d = inputValue3;
        e = inputValue4;
        f = inputValue5;
        g = inputValue6;
        print(a)
        print(b)

        ani = mysql.connector.connect(
            host="192.168.150.68",
            user="an",
            passwd="an",
            database="employee"
        )
        pyt = mysql.connector.connect(
            host="192.168.150.70",
            user="anp",
            passwd="an",
            database="codesena"
        )

        ani_wid = mysql.connector.connect(
            host="192.168.150.68",
            user="an",
            passwd="an",
            database="employee"
        )
        py_wid = mysql.connector.connect(
            host="192.168.150.70",
            user="anp",
            passwd="an",
            database="codesena"
        )

        mycursor1 = ani.cursor()
        mycursor2 = pyt.cursor()
        mycursor3 = ani_wid.cursor()
        mycursor4 = py_wid.cursor()
        sql1 = "INSERT INTO userlist (FirstName,MiddleName,LastName,username,Password,E_mail,Mobile,otp) VALUES (%s, %s,%s, %s,%s, %s,%s,%s)"
        sql = "INSERT INTO data (First_Name,Middle_Name,Last_Name,username,Password,Email,Mobile_no,otp) VALUES (%s, %s,%s, %s,%s, %s,%s,%s)"
        val = (a, b, c, d, e, f, g, "1234")

        wid = hashlib.sha256(a.encode()).hexdigest()
        wid_sql = "INSERT INTO wid (username,wid,balance) VALUES (%s, %s,%s)"
        wid_val = (d, wid, 0);
        mycursor1.execute(sql1, val)
        mycursor2.execute(sql, val)
        print("record inserted.")
        mycursor3.execute(wid_sql, wid_val)
        mycursor4.execute(wid_sql, wid_val)
        print("Wid Genrated")
        pyt.commit()
        ani.commit()
        ani_wid.commit()
        py_wid.commit()
        exit()

    cscoin = tkinter.Label(root, text="CSCOIN", font="50",fg="blue").place(x=150, y=50)
    First_Name = tkinter.Label(root, text="First Name :",fg="blue").place(x=30, y=100)
    Middle_Name = tkinter.Label(root, text="Middle Name :",fg="blue").place(x=30, y=150)
    Last_Name = tkinter.Label(root, text="Last Name :",fg="blue").place(x=30, y=200)
    Username = tkinter.Label(root, text="Username :",fg="blue").place(x=30, y=250)
    Password = tkinter.Label(root, text="password :",fg="blue").place(x=30, y=300)
    Email = tkinter.Label(root, text="Email :",fg="blue").place(x=30, y=350)
    Mobile_Number = tkinter.Label(root, text="Mobile Number :",fg="blue").place(x=30, y=400)
    # Conform_Password = tkinter.Label(root, text="Conform Password").place(x=30, y=450)

    textBox = Text(root, height=1, width=13)
    textBox.place(x=250, y=100)
    textBox1 = Text(root, height=1, width=13)
    textBox1.place(x=250, y=150)
    textBox2 = Text(root, height=1, width=13)
    textBox2.place(x=250, y=200)
    textBox3 = Text(root, height=1, width=13)
    textBox3.place(x=250, y=250)
    textBox4 = Text(root, height=1, width=13)
    textBox4.place(x=250, y=300)
    textBox5 = Text(root, height=1, width=13)
    textBox5.place(x=250, y=350)
    textBox6 = Text(root, height=1, width=13)
    textBox6.place(x=250, y=400)
    # textBox6 = Text(root, height=1, width=13)
    # textBox6.place(x=250, y=450)

    buttonCommit = Button(root, height=1, width=10, text="Submit",
                          command=lambda: retrieve_input(),fg="blue")
    buttonCommit.place(x=150, y=500)

    mainloop()

#--------------------CODE STARTED---------------------------------
login=tkinter.Tk()
login.geometry("400x300")
login.title('login page')
username = tkinter.Label(login, text ="Welcome to CSCOIN",fg="Blue",font="30").place(x = 125, y = 30)
username1 = tkinter.Label(login, text ="Username :",fg="blue").place(x = 80, y = 80)
textBo = Text(login, height=1, width=13,bd=2)
textBo.place(x=180, y=80)
textBo1 = Text(login, height=1, width=13,bd=2)
textBo1.place(x=180, y=150)
password = tkinter.Label(login, text ="password :",fg="blue").place(x = 80, y = 150)
Loginbtn = tkinter.Button(login, text ="  Login   ",fg="blue",command=loginp).place(x = 130, y =230)

button = tkinter.Button(login, text="Sign Up",fg="blue",command=signup1).place(x=200, y=230)

login.resizable(False,False)
login.mainloop()



