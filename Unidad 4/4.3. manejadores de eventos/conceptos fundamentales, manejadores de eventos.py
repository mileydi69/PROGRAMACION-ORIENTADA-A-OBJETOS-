import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista inicial de tareas
        self.task_list = ["ir al banco", "hacer el desayuno mañana", "ir al doctor"]

        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(root, width=20)
        self.entry.grid(row=0, column=0, padx=5, pady=5)
        self.entry.bind("<Return>", self.add_task_event)  # Añadir tarea con la tecla Enter

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        # Listbox para mostrar las tareas
        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Botón para marcar como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_as_completed)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        # Inicializar la lista de tareas en el Listbox
        self.update_task_listbox()

    # Función para añadir tarea
    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.task_list.append(task)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

    # Evento para añadir tarea al presionar Enter
    def add_task_event(self, event):
        self.add_task()

    # Función para marcar tarea como completada
    def mark_as_completed(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task = self.task_list[selected_task_index[0]]
            completed_task = f"{task} (Completada)"
            self.task_list[selected_task_index[0]] = completed_task
            self.update_task_listbox()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

    # Función para eliminar tarea
    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.task_list.pop(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

    # Función para actualizar la lista de tareas en el Listbox
    def update_task_listbox(self):
        self.listbox.delete(0, tk.END)  # Borra todo el contenido actual
        for task in self.task_list:
            self.listbox.insert(tk.END, task)  # Inserta cada tarea en la lista


# Crear la ventana principal
root = tk.Tk()
app = TodoApp(root)

# Iniciar el bucle principal
root.mainloop()







