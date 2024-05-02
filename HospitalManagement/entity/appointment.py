class Appointment:
    def __init__(self, appointmentId, patientId, doctorId, appointmentDate, description):
        self.appointmentId = appointmentId
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentDate = appointmentDate
        self.description = description

    # Getters and setters
    def getAppointmentId(self):
        return self.appointmentId

    def setAppointmentId(self, appointmentId):
        self.appointmentId = appointmentId

    def getPatientId(self):
        return self.patientId

    def setPatientId(self, patientId):
        self.patientId = patientId

    def getDoctorId(self):
        return self.doctorId

    def setDoctorId(self, doctorId):
        self.doctorId = doctorId

    def getAppointmentDate(self):
        return self.appointmentDate

    def setAppointmentDate(self, appointmentDate):
        self.appointmentDate = appointmentDate

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def __str__(self):
        return f"Appointment ID: {self.appointmentId}, Patient ID: {self.patientId}, Doctor ID: {self.doctorId} \nAppointment Date: {self.appointmentDate}, Description: {self.description}"