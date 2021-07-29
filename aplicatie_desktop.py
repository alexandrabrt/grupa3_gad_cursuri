# import tkinter
# from tkinter import *
#
#
# # window.title('Prima noastra aplicatie')
# # label = tkinter.Label(window, text="Text").pack()
# # button = tkinter.Button(window, text='Click')
# # button.pack()
# #
# # checkbox1 = IntVar()
# # checkbox2 = IntVar()
# # tkinter.Checkbutton(window, text="Text1", variable=checkbox1, onvalue=1, offvalue=0).grid(row=0, sticky=W)
# # tkinter.Checkbutton(window, text='Text2', variable=checkbox2, onvalue=0, offvalue=1).grid(row=1, sticky=W)
#
# # tkinter.Label(window, text='Username').grid(row=0)
# # tkinter.Entry(window).grid(row=0, column=1)
# #
# # tkinter.Label(window, text='Password').grid(row=1)
# # tkinter.Entry(window, show='*').grid(row=1, column=1)
# #
# # tkinter.Checkbutton(window, text="Tine-ma minte").grid(columnspan=2)
#
# window = tkinter.Tk()
# window.geometry('200x100')
#
# def left_click(event):
#     tkinter.Label(window, text="Left click!").pack()
#
#
# def middle_click(event):
#     tkinter.Label(window, text="Middle click!").pack()
#
#
# def right_click(event):
#     tkinter.Label(window, text='Right click').pack()
#
# window.bind("<Button-1>", left_click)
# window.bind("<Button-2>", middle_click)
# window.bind("<Button-3>", right_click)
#
# # def buton2(event):
# #     print(f'Button-2 apasat la x = {event.x}, y = {event.y}')
# #
# #
# # def buton3(event):
# #     print(f'Button-3 apasat la x = {event.x}, y = {event.y}')
# #
# #
# # def dublu_click(event):
# #     print(f'Dublu click apasat la x = {event.x}, y = {event.y}')
# #
# #
# # frame1 = Frame(window, height=100, width=200)
# # frame1.bind('<Button-2>', buton2)
# # frame1.bind('<Button-3>', buton3)
# # frame1.bind('<Double 1>', dublu_click)
# # frame1.pack()
#
# window.mainloop()

# from setuptools import setup
# setup(
#     app=["calculator_tkinter.py"],
#     setup_requires=["py2app"],
# )
