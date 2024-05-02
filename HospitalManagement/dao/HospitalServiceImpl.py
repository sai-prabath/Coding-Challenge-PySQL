from mysql.connector import Error
from HospitalManagement.entity.appointment import Appointment
from HospitalManagement.dao.IHospitalService import IHospitalService
from HospitalManagement.util.dbutil import DBConnection
from HospitalManagement.exception.MyExceptions import PatientNumberNotFoundException, AppointmentNotFoundException

class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        self.connection = DBConnection.getConnection()

    def getAppointmentById(self, appointmentId):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Appointment WHERE appointmentId = %s"
            cursor.execute(query, (appointmentId,))
            appointment_data = cursor.fetchone()
            cursor.close()
            if appointment_data:
                appointment = Appointment(*appointment_data)
                return appointment
            else:
                raise AppointmentNotFoundException(f"Appointment with ID {appointmentId} not found.")
        except Error as e:
            print("Error Fetching Appointment: ", e)
            return None

    def getAppointmentsForPatient(self, patientId):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Appointment WHERE patientId = %s"
            cursor.execute(query, (patientId,))
            appointment_data = cursor.fetchall()
            cursor.close()
            appointments = [Appointment(*data) for data in appointment_data]
            return appointments
        except PatientNumberNotFoundException as e:
            print("Error Fetching Appointments: ", e)
            return []
        except Error as e:
            print("Error Fetching Appointments: ", e)
            return []

    def getAppointmentsForDoctor(self, doctorId):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Appointment WHERE doctorId = %s"
            cursor.execute(query, (doctorId,))
            appointment_data = cursor.fetchall()
            cursor.close()
            appointments = [Appointment(*data) for data in appointment_data]
            return appointments
        except Error as e:
            print("Error Fetching Appointments: ", e)
            return []

    def scheduleAppointment(self, appointment):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Appointment (patientId, doctorId, appointmentDate, description) VALUES (%s, %s, %s, %s)"
            values = (appointment.patientId, appointment.doctorId, appointment.appointmentDate, appointment.description)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print("Error scheduling Appointment:", e)
            return False

    def updateAppointment(self, appointment):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Appointment SET patientId = %s, doctorId = %s, appointmentDate = %s, description = %s WHERE appointmentId = %s"
            values = (appointment.patientId, appointment.doctorId, appointment.appointmentDate, appointment.description, appointment.appointmentId)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print("Error updating Appointment:", e)
            return False

    def cancelAppointment(self, appointmentId):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Appointment WHERE appointmentId = %s"
            cursor.execute(query, (appointmentId,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print("Error:", e)
            return False

    def addPatient(self, patient):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Patient (firstName, lastName, dateOfBirth, gender, contactNumber, address) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (patient.getFirstName(), patient.getLastName(), patient.getDateOfBirth(), patient.getGender(),
                      patient.getContactNumber(), patient.getAddress())
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print("Error Adding Patient:", e)
            return False

    def addDoctor(self, doctor):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Doctor (firstName, lastName, specialization, contactNumber) VALUES (%s, %s, %s, %s)"
            values = (
                doctor.getFirstName(), doctor.getLastName(), doctor.getSpecialization(), doctor.getContactNumber())
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print("Error Adding Doctor:", e)
            return False


