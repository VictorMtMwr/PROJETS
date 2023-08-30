class Patient:
    def __init__(self, ID, Name, Sex, dateB, arterialPresion, arterialPresion2,
                 temperature, saturation, frecuency, notes, diagnosticImage,
                 examResults, prescriptionDrugs):
        self.ID = ID
        self.Name = Name
        self.Sex = Sex
        self.dateB = dateB
        self.arterialPresion = arterialPresion
        self.arterialPresion2 = arterialPresion2
        self.temperature = temperature
        self.saturation = saturation
        self.frecuency = frecuency
        self.notes = notes
        self.diagnosticImage = diagnosticImage
        self.examResults = examResults
        self.prescriptionDrugs = prescriptionDrugs
        self.a = "Enfermedad pulmonar obstructiva crónica EPOC"
        self.b = "Hipertension arterial"
        self.antecedents = []

    def input_data(self):
        print("****************REGISTRAR PACIENTES****************")
        ID = str(input("Digite el numero de cedula del paciente a ingresar: "))
        Name = str(input("Digite el nombre del paciente: "))
        Sex = ""
        while Sex.upper() not in ["M", "F"]:
            Sex = str(input("Sexo M/F: "))
            if Sex.upper() not in ["M", "F"]:
                print("Sexo inválido. Por favor, ingrese M o F.")

        dateB = ""
        while not Patient.validate_date_format(self, dateB):
            dateB = str(input("Fecha de nacimiento (DD/MM/AA): "))
            if not Patient.validate_date_format(self, dateB):

                print("Formato de fecha inválido. "
                      "Ingrese en el formato DD/MM/AA: ")

        arterialPresion = int(input("Digite la presion "
                                    "arterial del paciente: "))
        arterialPresion2 = int(input("/ "))
        temperature = int(input("Digite la temperatura del paciente: "))
        saturation = int(input("Digite el numero de saturacion"
                               " de O2 del paciente en %: "))
        frecuency = int(input("Digite la frecuencia "
                              "respiratoria del paciente: "))
        notes = str(input("Notas de evolucion del paciente: "))
        diagnosticImage = str(input("Imagenes diagnosticas"
                                    " realizadas al paciente: "))
        examResults = str(
            input("Resultados de los examenes"
                  " realizados al paciente: "
                  )
                        )
        prescriptionDrugs = str(input("Medicamentos formulados al paciente: "))

        patient = Patient(ID, Name, Sex, dateB, arterialPresion,
                          arterialPresion2, temperature, saturation,
                          frecuency, notes, diagnosticImage, examResults,
                          prescriptionDrugs)

        self.patient_list.append(patient)
        patient.determine_diseases()

    def validate_date_format(self, date_str):
        components = date_str.split('/')
        if len(components) != 3:
            return False
        day, month, year = components
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            return False
        day = int(day)
        month = int(month)
        year = int(year)
        if not (1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 9999):
            return False
        return True

    def determine_diseases(self):
        print("El paciente puede sufrir las"
              " siguientes enfermedades cronicas: ")
        if self.arterialPresion >= 130 and self.arterialPresion2 >= 80:
            print(self.b)
            if self.ID not in self.antecedents:
                self.antecedents.append(self.ID)
                self.aux = 1
        else:
            return None

        if self.saturation < 90 and (self.frecuency > 20
                                     or self.frecuency < 12):
            print(self.a)
            if self.ID not in self.antecedents:
                self.antecedents.append(self.ID)
                self.aux += 1

        else:
            return None

    def print_antecedents(self):
        if self.antecedents:
            print("Pacientes con enfermedades crónicas:")
            for patient_id in self.antecedents:
                print("ID:", patient_id, "\nNombre: ", self.Name)
                print("Enfermedades crónicas:", "\n", self.a, "\n", self.b)
                print("Medicamentos recetados:", self.prescriptionDrugs)
        else:
            return None
