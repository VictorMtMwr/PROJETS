from patient import Patient


class Beds():

    def __init__(self,):
        """
        Constructor method by Beds class.
        """
        self.numberBeds = 300
        self.percentOcupation = 0
        Patient.validate_date_format()

    def nBeds(self, patient_list):
        """
            This method determines the availability
            of beds and hospital occupancy.
        """
        self.numberBeds = 300 - len(patient_list)
        print("****Hospital San Vicente****")
        print("Hay ", self.numberBeds,
              " Camas disponibles en el hospital")
        percentOcupation = 100 - (((self.numberBeds) / 300) * 100)
        print("El porcentaje de ocupacion "
              "de camas es: ", round(percentOcupation, 2), "%")

    def out(self, searcher):
        """
            This method allows to discharge a patient.
        """
        print("********DAR DE ALTA A UN PACIENTE**********")
        found = False
        for patient in self.patient_list:
            if patient.ID == searcher:
                found = True
                self.patient_list.remove(patient)
                print("***********PACIENTE DADO DE ALTA CON EXITO*********")
                self.count += 1
                break
        if not found:
            print("__________________________________________________")
            print("Usuario no encontrado. Intente nuevamente")
            print("__________________________________________________")

    def in_out(self):
        print("El numero de admisiones actual es de: ", self.nAdmission)
        print("El numero de altas por servicios actual es de: ", self.count)
