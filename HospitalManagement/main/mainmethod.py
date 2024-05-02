from HospitalManagement.dao.HospitalServiceImpl import HospitalServiceImpl
from HospitalManagement.entity.appointment import Appointment
from HospitalManagement.entity.doctor import Doctor
from HospitalManagement.entity.patient import Patient

class MainModule:
    def __init__(self):
        self.hospital_service = HospitalServiceImpl()

    def display_menu(self):
        print("\nWelcome to the Hospital Management System!")
        print("1. Get Appointment by ID")
        print("2. Get Appointments for Patient")
        print("3. Get Appointments for Doctor")
        print("4. Schedule Appointment")
        print("5. Update Appointment")
        print("6. Cancel Appointment")
        print("7. Add Doctor")
        print("8. Add Patient")
        print("9. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.get_appointment_by_id()
            elif choice == "2":
                self.get_appointments_for_patient()
            elif choice == "3":
                self.get_appointments_for_doctor()
            elif choice == "4":
                self.schedule_appointment()
            elif choice == "5":
                self.update_appointment()
            elif choice == "6":
                self.cancel_appointment()
            elif choice == "7":
                self.add_doctor()
            elif choice == "8":
                self.add_patient()
            elif choice == "9":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_appointment_by_id(self):
        appointment_id = input("Enter the Appointment ID: ")
        appointment = self.hospital_service.getAppointmentById(appointment_id)
        if appointment:
            print(appointment)
        else:
            print(f"Appointment id {appointment_id} not found.")

    def get_appointments_for_patient(self):
        patient_id = input("Enter the Patient ID: ")
        appointments = self.hospital_service.getAppointmentsForPatient(patient_id)
        if appointments:
            for appointment in appointments:
                print(appointment)
        else:
            print("No appointments found for the patient.")

    def get_appointments_for_doctor(self):
        doctor_id = input("Enter the Doctor ID: ")
        appointments = self.hospital_service.getAppointmentsForDoctor(doctor_id)
        if appointments:
            for appointment in appointments:
                print(appointment)
        else:
            print("No appointments found for the doctor.")

    def schedule_appointment(self):
        try:
            patient_id = input("Enter Patient ID: ")
            doctor_id = input("Enter Doctor ID: ")
            appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
            description = input("Enter Description: ")
            appointment = Appointment(None, patient_id, doctor_id, appointment_date, description)

            if self.hospital_service.scheduleAppointment(appointment):
                print("Appointment scheduled successfully!")
            else:
                print("Failed to schedule appointment.")
        except Exception as e:
            print(f"Error: {e}")

    def update_appointment(self):
        try:
            appointment_id = input("Enter Appointment ID to update: ")
            appointment = self.hospital_service.getAppointmentById(appointment_id)
            if appointment:
                print(appointment)
                patient_id = input("Enter Patient ID to update: ")
                doctor_id = input("Enter Doctor ID to update: ")
                appointment_date = input("Enter new Appointment Date (YYYY-MM-DD): ")
                description = input("Enter new Description: ")
                appointment.setPatientId(patient_id)
                appointment.setDoctorId(doctor_id)
                appointment.setAppointmentDate(appointment_date)
                appointment.setDescription(description)

                if self.hospital_service.updateAppointment(appointment):
                    print("Appointment updated successfully!")
                else:
                    print("Failed to update appointment.")
        except Exception as e:
            print(f"Error : {e}")


    def cancel_appointment(self):
        try:
            appointment_id = input("Enter Appointment ID to cancel: ")

            if self.hospital_service.cancelAppointment(appointment_id):
                print("Appointment canceled successfully!")
            else:
                print("Failed to cancel appointment.")
        except Exception as e:
            print(f"Error canceling appointment: {e}")

    def add_patient(self):
        try:
            first_name = input("Enter Patient First Name: ")
            last_name = input("Enter Patient Last Name: ")
            date_of_birth = input("Enter Patient Date of Birth (YYYY-MM-DD): ")
            gender = input("Enter Patient Gender: ")
            contact_number = input("Enter Patient Contact Number: ")
            address = input("Enter Patient Address: ")
            patient = Patient(None, first_name, last_name, date_of_birth, gender, contact_number, address)

            if self.hospital_service.addPatient(patient):
                print("Patient added successfully!")
            else:
                print("Failed to add patient.")
        except Exception as e:
            print(f"Error adding patient: {e}")

    def add_doctor(self):
        try:
            first_name = input("Enter Doctor First Name: ")
            last_name = input("Enter Doctor Last Name: ")
            specialization = input("Enter Doctor Specialization: ")
            contact_number = input("Enter Doctor Contact Number: ")

            doctor = Doctor(None, first_name, last_name, specialization, contact_number)

            if self.hospital_service.addDoctor(doctor):
                print("Doctor added successfully!")
            else:
                print("Failed to add doctor.")
        except Exception as e:
            print(f"Error adding doctor: {e}")




