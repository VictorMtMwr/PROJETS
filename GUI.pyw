import tkinter as tk
from tkinter import ttk, messagebox
from hospital import Hospital
from patient import Patient


class HospitalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital San Vicente")
        self.root.geometry("320x300")
        self.root.configure(bg="#c5c5c5")

        style = ttk.Style()
        style.theme_use("winnative")  # Puedes cambiar el tema a tu preferencia

        self.hospital = Hospital()

        self.label = ttk.Label(root,
                               text="Sistema de Gestión Hospitalaria",
                               font=("Helvetica", 16)
                               )
        self.label.pack(pady=10)

        self.button_register = ttk.Button(root,
                                          text="Registrar Paciente",
                                          command=self.register_patient
                                          )
        self.button_register.pack()

        self.button_search = ttk.Button(root,
                                        text="Buscar Paciente",
                                        command=self.search_patient
                                        )
        self.button_search.pack()

        self.button_discharge = ttk.Button(root,
                                           text="Dar de Alta Paciente",
                                           command=self.discharge_patient
                                           )
        self.button_discharge.pack()

        self.button_occupation = ttk.Button(root,
                                            text="Mostrar Ocupación de Camas",
                                            command=self.show_occupation
                                            )
        self.button_occupation.pack()

        self.button_antic = ttk.Button(root,
                                       text="Pacientes con "
                                       "Enfermedades Crónicas",
                                       command=self.show_antecedents
                                       )
        self.button_antic.pack()

    def register_patient(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Registrar Paciente")

        ID_var = tk.StringVar()
        Name_var = tk.StringVar()
        Sex_var = tk.StringVar()
        Date_var = tk.StringVar()
        ArterialPresion_var = tk.IntVar()
        ArterialPresion2_var = tk.IntVar()
        Temperature_var = tk.IntVar()
        Saturation_var = tk.IntVar()
        Frecuency_var = tk.IntVar()
        Notes_var = tk.StringVar()
        DiagnosticImage_var = tk.StringVar()
        ExamResults_var = tk.StringVar()
        PrescriptionDrugs_var = tk.StringVar()

        tk.Label(register_window, text="ID del Paciente:").pack()
        tk.Entry(register_window, textvariable=ID_var).pack()

        tk.Label(register_window, text="Nombre del Paciente:").pack()
        tk.Entry(register_window, textvariable=Name_var).pack()

        tk.Label(register_window, text="Sexo (M/F):").pack()
        tk.Entry(register_window, textvariable=Sex_var).pack()

        tk.Label(register_window,
                 text="Fecha de Nacimiento (DD/MM/AA):"
                 ).pack()
        tk.Entry(register_window, textvariable=Date_var).pack()

        tk.Label(register_window, text="Presión Arterial:").pack()
        tk.Entry(register_window, textvariable=ArterialPresion_var).pack()

        tk.Label(register_window,
                 text="Presión Arterial (segundo valor):"
                 ).pack()
        tk.Entry(register_window, textvariable=ArterialPresion2_var).pack()

        tk.Label(register_window, text="Temperatura:").pack()
        tk.Entry(register_window, textvariable=Temperature_var).pack()

        tk.Label(register_window, text="Saturación de O2:").pack()
        tk.Entry(register_window, textvariable=Saturation_var).pack()

        tk.Label(register_window, text="Frecuencia Cardiaca:").pack()
        tk.Entry(register_window, textvariable=Frecuency_var).pack()

        tk.Label(register_window, text="Notas de Evolución:").pack()
        tk.Entry(register_window, textvariable=Notes_var).pack()

        tk.Label(register_window, text="Imágenes Diagnósticas:").pack()
        tk.Entry(register_window, textvariable=DiagnosticImage_var).pack()

        tk.Label(register_window, text="Resultados de Exámenes:").pack()
        tk.Entry(register_window, textvariable=ExamResults_var).pack()

        tk.Label(register_window, text="Medicamentos Recetados:").pack()
        tk.Entry(register_window, textvariable=PrescriptionDrugs_var).pack()

        def submit():
            ID = ID_var.get()
            Name = Name_var.get()
            Sex = Sex_var.get()
            Date = Date_var.get()
            ArterialPresion = ArterialPresion_var.get()
            ArterialPresion2 = ArterialPresion2_var.get()
            Temperature = Temperature_var.get()
            Saturation = Saturation_var.get()
            Frecuency = Frecuency_var.get()
            Notes = Notes_var.get()
            DiagnosticImage = DiagnosticImage_var.get()
            ExamResults = ExamResults_var.get()
            PrescriptionDrugs = PrescriptionDrugs_var.get()

            patient = Patient(ID, Name, Sex, Date, ArterialPresion,
                              ArterialPresion2,
                              Temperature, Saturation, Frecuency, Notes,
                              DiagnosticImage, ExamResults, PrescriptionDrugs)
            self.hospital.patient_list.append(patient)

            register_window.destroy()

        tk.Button(register_window, text="Registrar", command=submit).pack()

        register_window.mainloop()

    def search_patient(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Buscar Paciente")

        ID_var = tk.StringVar()

        tk.Label(search_window, text="Ingrese el ID del Paciente:").pack()
        tk.Entry(search_window, textvariable=ID_var).pack()

        result_text = tk.StringVar()
        result_label = tk.Label(search_window, textvariable=result_text)
        result_label.pack()

        def search():
            search_id = ID_var.get()
            found_patient = None

            for patient in self.hospital.patient_list:
                if patient.ID == search_id:
                    found_patient = patient
                    break

            if found_patient:
                result = f"ID: {found_patient.ID}\nNombre: {found_patient.Name}\nSexo: {found_patient.Sex}\nFecha de Nacimiento: {found_patient.dateB}\nPresión Arterial: {found_patient.arterialPresion}/{found_patient.arterialPresion2}\nTemperatura: {found_patient.temperature}\nSaturación de O2: {found_patient.saturation}\nFrecuencia Cardiaca: {found_patient.frecuency}\nNotas de Evolución: {found_patient.notes}\n"
                result_text.set(result)
            else:
                result_text.set("Paciente no encontrado")

        tk.Button(search_window, text="Buscar", command=search).pack()

        search_window.mainloop()

    def discharge_patient(self):
        discharge_window = tk.Toplevel(self.root)
        discharge_window.title("Dar de Alta Paciente")

        ID_var = tk.StringVar()

        tk.Label(discharge_window,
                 text="Ingrese el ID del Paciente a dar de alta:"
                 ).pack()
        tk.Entry(discharge_window, textvariable=ID_var).pack()

        result_text = tk.StringVar()
        result_label = tk.Label(discharge_window, textvariable=result_text)
        result_label.pack()

        def discharge():
            search_id = ID_var.get()
            found_patient = None

            for patient in self.hospital.patient_list:
                if patient.ID == search_id:
                    found_patient = patient
                    break

            if found_patient:
                self.hospital.patient_list.remove(found_patient)
                result_text.set("Paciente dado de alta con éxito.")
            else:
                result_text.set("Paciente no encontrado.")

        tk.Button(discharge_window,
                  text="Dar de Alta",
                  command=discharge
                  ).pack()

        discharge_window.mainloop()

    def show_occupation(self):
        n_beds = 300
        occupied_beds = len(self.hospital.patient_list)
        available_beds = n_beds - occupied_beds
        occupation_text = f"Camas ocupadas: {occupied_beds}\nCamas disponibles: {available_beds}"
        messagebox.showinfo("Ocupación de Camas", occupation_text)

    def show_antecedents(self):
        patients_with_antecedents = [
            patient for patient in self.hospital.patient_list
            if patient.ID in patient.antecedents
        ]
        if patients_with_antecedents:
            antecedents_text = "\n\n".join(patient.get_antecedents_text() for patient in patients_with_antecedents)
            messagebox.showinfo("Pacientes con Enfermedades Crónicas",
                                antecedents_text)
        else:
            messagebox.showinfo("Pacientes con Enfermedades Crónicas", "No hay pacientes con enfermedades crónicas.")


if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()
