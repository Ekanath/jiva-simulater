from tkinter import *

a = Tk()
a.title('Game- 01 v0.01')

# evergy_value_c
INITIAL_VALUE = 100
evergy_value_c = INITIAL_VALUE
health_value_c = INITIAL_VALUE
money_value_c = INITIAL_VALUE
wisdom_value_c = 0
time_value_c = 2400
progress_value_c = 'Idel '


def eat():
    global health_value_c
    global money_value_c
    global evergy_value_c
    global progress_value_c

    if health_value_c > 5 and money_value_c >= 10:
        health_value_c += 10
        money_value_c -= 10
        evergy_value_c += 25
        progress_value_c = 'Sleeping.....ZzZzzzZzzz'
        # replacing the labels
        energy_value_label = Label(a, text=evergy_value_c).grid(row=1, column=0)
        money_value_label = Label(a, text=money_value_c).grid(row=1, column=2)
        health_value_label = Label(a, text=health_value_c).grid(row=1, column=1)
        progress_label = Label(a, text=progress_value_c, ).grid(row=5, column=0)
        print(' Eating ')

    elif health_value_c == 0:
        print('Died')




def work():
    global evergy_value_c
    global money_value_c
    global health_value_c
    global progress_value_c

    if evergy_value_c >= 55 and not evergy_value_c < 54:
        evergy_value_c -= 20
        money_value_c += 30
        health_value_c += 5
        progress_value_c = 'Working.....'
        energy_value_label = Label(a, text=evergy_value_c).grid(row=1, column=0)
        health_value_label = Label(a, text=health_value_c).grid(row=1, column=1)
        money_value_label = Label(a, text=money_value_c).grid(row=1, column=2)
        progress_label = Label(a, text=progress_value_c, ).grid(row=5, column=0)
        print('Working')


def sleep():
    global progress_value_c

    print ( ' Buzzz.....Sleeping' )
    pass


# ==============Labels=============================================Labels

# Energy label
energy_label = Label(a, text=" Energy ", bg='white').grid(row=0, column=0)
# Energy value label
energy_value_label = Label(a, text=evergy_value_c, ).grid(row=1, column=0)

# Health label
health_label = Label(a, text=" Health ").grid(row=0, column=1)
# Health value label
health_value_label = Label(a, text=health_value_c).grid(row=1, column=1)

# Money label
money_label = Label(a, text=" Money ").grid(row=0, column=2)
# Money value label
money_value_label = Label(a, text= money_value_c).grid(row=1, column=2)

# Wisdom label
wisdom_label = Label(a, text=" Wisdom ").grid(row=0, column=3)
# Money value label
wisdom_value_label = Label(a, text=wisdom_value_c).grid(row=1, column=3)

# Time label
wisdom_label = Label(a, text=" Time ").grid(row=0, column=4)
# Time value label
wisdom_value_label = Label(a, text= time_value_c ).grid(row=1, column=4)

#=================Current Label======
progress_label = Label(a, text = progress_value_c, ).grid(row=5 ,column= 0)

# =============Butttons===============================================buttons
# eat button
btn_eat = Button(a, text="     Eat     ", command= eat).grid(row=2, column=0)
btn_work = Button(a, text="     Work    ", command= work).grid(row=3, column=0)
btn_sleep = Button(a, text="     Sleep   " , command = sleep).grid(row=4, column=0)
a.mainloop()
