import tkinter as tk
from tkinter import filedialog, messagebox
from docxtpl import DocxTemplate
import jinja2
import csv
from datetime import datetime

# Fonction pour convertir les dates
def datetimeformat(value, format="%H:%M %d-%m-%y"):
    if isinstance(value, str):
        value = datetime.strptime(value, "%Y-%m-%d")
    return value.strftime(format)

jinja2.filters.FILTERS['datetimeformat'] = datetimeformat

context_csv_path = None  # Store the context CSV path

# Charge les champs
def load_context_from_csv(csv_path):
    context = {}
    with open(csv_path, 'r', newline='', encoding='ISO8859-1') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        field_names = next(csvreader)
        values = next(csvreader)
        
        for field, value in zip(field_names, values):
            # Permet de détecter si la valeur est numérique
            if value.replace(".", "", 1).isdigit():
                
                if "." in value:
                    context[field] = float(value)
                else:
                    context[field] = int(value)
            else:
                context[field] = value
        
    return context

# Génère le fichier de sortie
def render_template(template_path, context, output_path):
    try:
        # Template Docx
        doc = DocxTemplate(template_path)

        doc.render(context)

        # Save the rendered template to the specified location
        doc.save(output_path)
        
        messagebox.showinfo("Info", f"Modèle généré et enregistré sous {output_path} !")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

# Charger le modèle source
def select_template():
    template_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
    if template_path:
        render_button.config(state=tk.NORMAL)  # Enable the render button
        template_label.config(text=f"Modèle : {template_path}")
        render_template_path.set(template_path)  # Set the template path for rendering

# Charger les champs
def load_context():
    global context_csv_path  # Use the global variable
    context_csv_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if context_csv_path:
        context = load_context_from_csv(context_csv_path)
        context_text.delete("1.0", tk.END)  # Clear previous context
        for field, value in context.items():
            context_text.insert(tk.END, f"{field}: {value}\n")
        
        context_label.config(text=f"Champs : {context_csv_path}")

# Génère le fichier de sortie
def render_selected_template():
    template_path = render_template_path.get()
    if template_path and context_csv_path:  # Use the stored context CSV path
        context = load_context_from_csv(context_csv_path)

        # Demander à l'utilisateur où enregistrer le fichier généré
        output_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Documents Word", "*.docx")])

        if output_path:
            doc = render_template(template_path, context, output_path)

            # Ask user if they want to open the rendered file
            open_file = messagebox.askyesno("Ouvrir le fichier", "Voulez-vous ouvrir le fichier généré ?")
            if open_file:
                import os
                os.system(output_path)
     

# Create the main UI window
root = tk.Tk()
root.title("Générateur de document")

# Add a button to select a template file
select_button = tk.Button(root, text="Sélectionner le modèle", command=select_template)
select_button.pack(padx=10, pady=10)

# Label to show selected template
template_label = tk.Label(root, text="Modèle :")
template_label.pack()

# Button to load the context
load_context_button = tk.Button(root, text="Charger les champs", command=load_context)
load_context_button.pack(padx=10, pady=5)

context_label = tk.Label(root, text="Champs :")
context_label.pack()

# Text widget to display and edit context
context_text = tk.Text(root, height=10, width=40)
context_text.pack(padx=10, pady=10)

# Button to render the selected template
render_template_path = tk.StringVar()  # Variable to store the selected template path
render_button = tk.Button(root, text="Générer le document", command=render_selected_template, state=tk.DISABLED)
render_button.pack(padx=10, pady=10)

# Start the main loop
root.mainloop()
