import tkinter as tk
from tkinter import messagebox

class TaskManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Tareas")

        self.tasks = []
        self.completed_tasks = set()  # Usamos un set para almacenar los índices de tareas completadas

        # Campo de entrada
        self.task_entry = tk.Entry(self, width=40)
        self.task_entry.pack(pady=10)

        # Botones
        self.add_button = tk.Button(self, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Listbox para mostrar tareas
        self.task_listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Eventos de teclado
        self.task_entry.bind('<Return>', lambda event: self.add_task())
        self.bind('<c>', lambda event: self.complete_task())
        self.bind('<Delete>', lambda event: self.delete_task())
        self.bind('<Escape>', lambda event: self.quit())

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            if selected_index in self.completed_tasks:
                messagebox.showinfo("Información", "Esta tarea ya está completada.")
                return

            self.completed_tasks.add(selected_index)  # Marcar la tarea como completada
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            if selected_index in self.completed_tasks:
                self.completed_tasks.remove(selected_index)  # Remover la tarea si está completada
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            if i in self.completed_tasks:
                # Mostrar la tarea completada con un checkmark
                self.task_listbox.insert(tk.END, f"✓ {task}")
                self.task_listbox.itemconfig(tk.END, {'fg': 'green'})  # Cambiar color a verde para completadas
            else:
                self.task_listbox.insert(tk.END, task)
                self.task_listbox.itemconfig(tk.END, {'fg': 'black'})  # Color negro para tareas pendientes

if __name__ == "__main__":
    app = TaskManager()
    app.mainloop()


