from tkinter import *
import pytube
from tkinter import messagebox
import os

def download():
    try:
        ytlink=link1.get()
        youtubelink=pytube.YouTube(ytlink, on_progress_callback=progress_function)
        video=youtubelink.streams.get_highest_resolution()
        download_directory = os.path.join(os.path.expanduser('~'), 'Downloads')
        video.download(download_directory)
        Result="Загрузка завершена"
        messagebox.showinfo("Готово", Result)
    except:
        Result="Ссылка не работает"
        messagebox.showerror("Ошибка", Result)

def progress_function(stream=None, chunk=None, bytes_remaining=None):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)

def reset():
    link1.set("")

def Exit():
    root.destroy()

root=Tk()
root.geometry("500x250")
root.resizable(False,False)
root.title("Код")
root.config(bg='#D3D3D3')

lb=Label(root, text="---загрузка видео с YouTube---",font=('Arial,15,bold'),bg='#D3D3D3')
lb.pack(pady=15)

lb1=Label(root, text="Ссылка на видео :", font=('Arial,15,bold'), bg='#D3D3D3')
lb1.place(x=10, y=80)

link1=StringVar()
En1=Entry(root,textvariable=link1,font=('Arial,15,bold'))
En1.place(x=230, y=80)

btn1=Button(root,text="Скачать", font=('Arial,10,bold'),bd=4,command=download)
btn1.place(x=330,y=130)

btn2=Button(root,text="Очистить", font=('Arial,10,bold'), bd=4, command=reset)
btn2.place(x=160,y=190)

btn3=Button(root,text="Выход", font=('Arial,10,bold'), bd=4, command=Exit)
btn3.place(x=250,y=190)

root.mainloop()
