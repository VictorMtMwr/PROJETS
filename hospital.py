from patient import Patient
from beds import Beds
from os import system
import datetime


class Hospital:

    def __init__(self):
        """
            Constructor method by Hospital
        """
        self.count = 0
        self.nAdmission = 0
        self.discharge_time_str = ""
        self.patient_list = []
        self.date_in = []

    def search_data(self):
        """
            This method allows the search for a patient by their
            identification number to provide a summary of their medical
            history.

        """
        print("*****************BUSCAR PACIENTE******************")
        searcher = input("Digite el numero de cedula del paciente: ")
        found = False

        for patient in self.patient_list:
            if patient.ID == searcher:
                found = True
                print("__________________________________________________")
                print("****************HISTORIA CLINICA******************")
                print("Paciente encontrado:")
                print("ID:", patient.ID)
                print("Nombre:", patient.Name)
                print("Sexo:", patient.Sex)
                print("Fecha de nacimiento:", patient.dateB)
                print("Presión arterial:", patient.arterialPresion)
                print("Temperatura:", patient.temperature)
                print("Saturación de O2:", patient.saturation)
                print("Frecuencia cardiaca:", patient.frecuency)
                print("Evolución:", patient.notes)
                print("Imagenes diagnósticas:", patient.diagnosticImage)
                print("Resultados de exámenes:", patient.examResults)
                print("Medicamentos recetados:", patient.prescriptionDrugs)
                patient.determine_diseases()
                print("__________________________________________________")
                break

        if not found:
            print("__________________________________________________")
            print("Usuario no encontrado. Intente nuevamente")
            print("__________________________________________________")

    def main(self):
        """
            Menu Main.
        """
        res = 0
        while res == 0:
            print("__________________________________________________")
            print("*********Hospital San Vicente*********")
            print("1. REGISTRO DE PACIENTE               ")
            print("2. BUSCAR PACIENTE                    ")
            print("3. OCUPACION HOSPITALARIAS            ")
            print("4. DAR DE ALTA A UN PACIENTE          ")
            print("5. PACIENTES CON ENFERMEDADES CRONICAS")
            print("6. SALIR                              ")
            res = int(input("Digite una opcion: "))
            print("__________________________________________________")
            if res == 1:
                system("cls")
                Patient.input_data(self)
                self.nAdmission += 1
                date_in = datetime.datetime.now()
                self.date_in.append(date_in)
                system("cls")
                print(self.date_in)
                print("************PACIENTE INGRESADO CON EXITO*************")
                res = 0
            elif res == 2:
                system("cls")
                self.search_data()
                res = 0
            elif res == 3:
                system("cls")
                Beds.nBeds(self, self.patient_list)
                Beds.in_out(self)
                res = 0
            elif res == 4:
                system("cls")
                searcher = input("Digite el numero de cedula del paciente: ")
                Beds.out(self)
                paciente_index = -1
                for i, paciente in enumerate(self.patient_list):
                    if paciente.ID == searcher:
                        paciente_index = i
                        break

                if paciente_index != -1:
                    fecha_actual = datetime.datetime.now()
                    tiempo_hospitalizacion = fecha_actual
                    - self.date_in[paciente_index]
                    print(f"El paciente ha estado en el hospital durante: {tiempo_hospitalizacion}")
                res = 0
            elif res == 5:
                system("cls")
                patients_with_antecedents = [
                    patient for patient in self.patient_list
                    if patient.ID in patient.antecedents
                ]
                if patients_with_antecedents:
                    for patient in patients_with_antecedents:
                        patient.print_antecedents()
                else:
                    print("No hay pacientes con enfermedades crónicas.")
                res = 0
            elif res == 6:
                break
            else:
                print("******RESPUESTA INVÁLIDA, INTENTE NUEVAMENTE******")
                res = 0
