import tkinter as tk
import socket
import platform


nombre_equipo = socket.gethostname()
direccion_equipo = socket.gethostbyname(nombre_equipo)

window = tk.Tk()
window.title("SO Data Informer")
window.geometry("500x350")

title = tk.Label(text="SO Information v.1 \n")
title.pack()

ip = tk.Label(text="Your Ip:")
ip.pack()
button = tk.Button(text="La IP es: %s" % direccion_equipo)
button.pack()

ne = tk.Label(text="Your PC Name:")
ne.pack()
button = tk.Button(text=socket.gethostname())
button.pack()

plso = tk.Label(text="Your SO Version:")
plso.pack()
button = tk.Button(text=platform.platform())
button.pack()

plsore = tk.Label(text="Your SO Release Version:")
plsore.pack()
button = tk.Button(text=platform.release())
button.pack()

mavs = tk.Label(text="Machine:")
mavs.pack()
button = tk.Button(text=platform.machine())
button.pack()

cre = tk.Label(text="\n" + "Github: @Bikz-0972")
cre.pack()

tk.mainloop()

### Discord: Bikz#0972
### More releases will be available
