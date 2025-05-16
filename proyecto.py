import tkinter as tk
from PIL import Image, ImageTk
import os
import random  

ventana = tk.Tk()
ventana.title("Monitor de Ambiente")
ventana.geometry("800x600") 


ruta_imagen = os.path.join("imagenes", "C:/Users/Usuario/Documents/Modulo Programacion/img/6023003.jpg")  # Asegúrate de tener una imagen relacionada
try:
    imagen_fondo = Image.open(ruta_imagen)
    imagen_fondo = imagen_fondo.resize((800, 600), Image.Resampling.LANCZOS)  
    fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    fondo_label = tk.Label(ventana, image=fondo_tk)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)  

except FileNotFoundError:
    print("Error: No se encontró la imagen de fondo.")


def actualizar_datos():
    
    temperatura = random.uniform(20.0, 30.0)
    humedad = random.uniform(40.0, 80.0)
    
    
    label_temp.config(text=f"Temperatura: {temperatura:.1f} °C")
    label_humedad.config(text=f"Humedad: {humedad:.1f} %")
    
    
    ventana.after(2000, actualizar_datos)


estilo_label = {
    "font": ("Arial", 24, "bold"),
    "bg": "#333333", 
    "fg": "white",    
    "borderwidth": 2,
    "relief": "ridge"
}


label_temp = tk.Label(ventana, **estilo_label)
label_temp.place(x=100, y=100, width=300, height=100)


label_humedad = tk.Label(ventana, **estilo_label)
label_humedad.place(x=100, y=250, width=300, height=100)


actualizar_datos()


ventana.mainloop()







