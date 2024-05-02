from abc import ABC, abstractmethod

class IHospitalService(ABC):
    @abstractmethod
    def getAppointmentById(self, appointmentId):
        pass

    @abstractmethod
    def getAppointmentsForPatient(self, patientId):
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self, doctorId):
        pass

    @abstractmethod
    def scheduleAppointment(self, appointment_obj):
        pass

    @abstractmethod
    def updateAppointment(self, appointment_obj):
        pass

    @abstractmethod
    def cancelAppointment(self, appointmentId) :
        pass

    @abstractmethod
    def addPatient(self, patient):
        pass

    @abstractmethod
    def addDoctor(self, doctor):
        pass


