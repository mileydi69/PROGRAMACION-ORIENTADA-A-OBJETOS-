import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Contenedor para la lista de eventos
        self.frame_list = tk.Frame(self.root)
        self.frame_list.pack(pady=10)

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_list, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Contenedor para entrada de datos
        self.frame_input = tk.Frame(self.root)
        self.frame_input.pack(pady=10)

        # Selección de fecha
        self.label_date = tk.Label(self.frame_input, text="Fecha:")
        self.label_date.grid(row=0, column=0)
        self.cal = Calendar(self.frame_input, selectmode='day')
        self.cal.grid(row=0, column=1)

        # Entrada de hora
        self.label_time = tk.Label(self.frame_input, text="Hora:")
        self.label_time.grid(row=1, column=0)
        self.entry_time = tk.Entry(self.frame_input)
        self.entry_time.grid(row=1, column=1)

        # Entrada de descripción
        self.label_desc = tk.Label(self.frame_input, text="Descripción:")
        self.label_desc.grid(row=2, column=0)
        self.entry_desc = tk.Entry(self.frame_input)
        self.entry_desc.grid(row=2, column=1)

        # Botones de acción
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.button_add = tk.Button(self.button_frame, text="Agregar Evento", command=self.add_event)
        self.button_add.grid(row=0, column=0, padx=5)

        self.button_delete = tk.Button(self.button_frame, text="Eliminar Evento Seleccionado",
                                       command=self.delete_event)
        self.button_delete.grid(row=0, column=1, padx=5)

        self.button_exit = tk.Button(self.button_frame, text="Salir", command=self.root.quit)
        self.button_exit.grid(row=0, column=2, padx=5)

    def add_event(self):
        date = self.cal.get_date()
        time = self.entry_time.get()
        description = self.entry_desc.get()

        if not time or not description:
            messagebox.showwarning("Advertencia", "llene los espacios en blanco.")
            return

        self.tree.insert("", "end", values=(date, time, description))
        self.entry_time.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def delete_event(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "esta tarde para el ingreso a clases")
            return

        confirm = messagebox.askyesno("Confirmar", "¿llegara a tiempo, si se va en el metro?")
        if confirm:
            for item in selected_item:
                self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.geometry("500x400")
    root.mainloop()

