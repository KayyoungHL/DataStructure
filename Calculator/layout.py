from tkinter import *

root = Tk()
root.title("KAY Calculator")
root.geometry("640x480") # 가로 * 세로

## Display frame----------------------------------------


## grid frame-------------------------------------------
#(, ), del, clear
btn_po = Button(root, text='(', width=5, height=2)
btn_pc = Button(root, text=')', width=5, height=2)
btn_del = Button(root, text='del', width=5, height=2)
btn_clear = Button(root, text='clear', width=5, height=2)

btn_po.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_pc.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_del.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_clear.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)


# e, ^, /, *
btn_exp = Button(root, text='e', width=5, height=2)
btn_equal = Button(root, text='^', width=5, height=2)
btn_div = Button(root, text='/', width=5, height=2)
btn_mul = Button(root, text='*', width=5, height=2)

btn_exp.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)


# 7, 8, 9, -
btn_7 = Button(root, text='7', width=5, height=2)
btn_8 = Button(root, text='8', width=5, height=2)
btn_9 = Button(root, text='9', width=5, height=2)
btn_sub = Button(root, text='-', width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)


# 4, 5, 6, +
btn_4 = Button(root, text='4', width=5, height=2)
btn_5 = Button(root, text='5', width=5, height=2)
btn_6 = Button(root, text='6', width=5, height=2)
btn_plus = Button(root, text='+', width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_plus.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)


# 1, 2, 3, enter
btn_1 = Button(root, text='1', width=5, height=2)
btn_2 = Button(root, text='2', width=5, height=2)
btn_3 = Button(root, text='3', width=5, height=2)
btn_enter = Button(root, text='enter', width=5, height=2)

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # rowspan 현 위치로부터 아래로 합치기


# 0, .
btn_0 = Button(root, text='0', width=5, height=2)
btn_point = Button(root, text='.', width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) # columnspan 현 위치로부터 아래로 합시치
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()