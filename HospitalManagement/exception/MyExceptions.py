class PatientNumberNotFoundException(Exception):
    def __init__(self, message="Patient number not found in the database"):
        self.message = message
        super().__init__(self.message)

class AppointmentNotFoundException(Exception):
    def __init__(self, message="Appointment not found in the database"):
        self.message = message
        super().__init__(self.message)