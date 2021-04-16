from patient.models import Patient
from hospital.models import Hospital
from logic.models import TrainData

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

from neo4jintegration.views import calculate_shortest_node_path


class DecisionTree:

    def __init__(self, patient):
        self.patient = patient
        self.ai_detection = self.ml_part()

    @staticmethod
    def normalize_data():
        for patient in Patient.objects.all():
            patient.patient_type = str(patient.patient_type).lower()
            patient.triage = str(patient.triage).lower()
            patient.category = str(patient.category).lower()
            patient.save()

    @staticmethod
    def get_list_of_hospital_in_range_of_patient(patient, minutes):
        hospital_in_this_area = []

        for hospital in Hospital.objects.all():
            result = calculate_shortest_node_path(patient.grid_x+patient.grid_y, hospital.grid_x+hospital.grid_y)
            cost_to_hospital = result["totalCost"]
            if cost_to_hospital <= minutes:
                hospital_in_this_area.append({
                    "hospital": hospital,
                    "result": result
                })

        # Sortowanie względem kosztu?
        return hospital_in_this_area

    # Machine Learning part
    # Machine learning predictions
    def ml_part(self):
        data = []
        target = []
        for trained_value in TrainData.objects.all():
            data.append(trained_value.data)
            target.append(trained_value.target_category)

        model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        model.fit(data, target)
        return model.predict([self.patient.notes])

    def checkHospitalHasCorrectType(self, hospital):
        print("checkHospitalHasCorrectType")
        return hospital.type.check_correct_type(self.ai_detection)

    def transportPatientOutOfArea(self):
        # @todo: Skierować go tam
        print("transportPatientOutOfArea")
        try:
            hospital = Hospital.objects.get(pk=8)
            self.patient.selected_hospital = hospital
            self.patient.save()
        except Hospital.DoesNotExist:
            pass

    def transportPatient(self, hospital):
        if hospital:
            print(f"transportPatient to hospital: {hospital.id} TYPE: {hospital.get_type()}")
            self.patient.selected_hospital = hospital
            self.patient.save()
        else:
            print(f"transportPatient hospital object empty.")

    def tryToTransportPatient(self, hospitals):
        print("tryToTransportPatient")

        hospitals_with_free_beds = []
        for hospital in hospitals:
            if hospital.free_beds > 0:
                hospitals_with_free_beds.append(hospital)

        if len(hospitals_with_free_beds) > 0:
            for hospital in hospitals_with_free_beds:
                if self.checkHospitalHasCorrectType(hospital):
                    print(f"Great! Hospital has correct type. Chosen hospital: {hospital.id}")
                    self.transportPatient(hospital)
                    self.patient.patient_transported_to_hospital_with_free_beds = True
                    self.patient.save()
                    break
            if not self.patient.patient_transported_to_hospital_with_free_beds:
                print("Not found any hospital with correct type of capabilities. Transport to first one of list")
                self.transportPatient(hospitals[0])
        else:
            print("Not found hospital with free beds")
            self.transportPatient(hospitals[0])

    def evacuateCivilianPatient(self):
        print("evacuateCivilianPatient")
        result = DecisionTree.get_list_of_hospital_in_range_of_patient(
            self.patient,
            60 if self.patient.triage == "immediate" else 120
        )
        all_hospital_in_range = [x["hospital"] for x in result]

        civilian_hospitals = []
        for x in all_hospital_in_range:
            if x.get_type() == "D":
                civilian_hospitals.append(x)

        if len(civilian_hospitals) > 0:
            if len(civilian_hospitals) > 1:
                self.tryToTransportPatient(civilian_hospitals)
            else:
                print("Found only one civilian hospital. Transport to that once...")
                self.transportPatient(civilian_hospitals[0])
        else:
            self.transportPatientOutOfArea()

    def evacuateMilitaryPatient(self):
        print("evacuateMilitaryPatient")
        result = DecisionTree.get_list_of_hospital_in_range_of_patient(
            self.patient,
            60 if self.patient.triage == "immediate" else 120
        )
        all_hospital_in_range = [x["hospital"] for x in result]

        military_hospitals = []
        for x in all_hospital_in_range:
            if x.get_type() == "A" or x.get_type() == "B" or x.get_type() == "C":
                military_hospitals.append(x)

        if len(military_hospitals) > 0:
            if len(military_hospitals) > 1:
                self.tryToTransportPatient(military_hospitals)
            else:
                print("Found only one military hospital. Transport to that once...")
                self.transportPatient(military_hospitals[0])
        else:
            print("Not found any military hospital.")

            civilian_hospitals = []
            for x in all_hospital_in_range:
                if x.get_type() == "D":
                    civilian_hospitals.append(x)

            if len(civilian_hospitals) > 0:
                if len(civilian_hospitals) > 1:
                    self.tryToTransportPatient(civilian_hospitals)
                else:
                    print("Found only one civilian hospital. Transport to that once...")
                    self.transportPatient(civilian_hospitals[0])
            else:
                print("Trying to evacuate military patient with delayed triage.")

                if not self.patient.tried_evacute_immediate_with_result:
                    self.patient.tried_evacute_immediate_with_result = True
                    self.patient.save()
                    self.evacuateDelayed()
                else:
                    print("Tried evacuate patient IMMEDIATE and DELAYED FAILURE")
                    self.transportPatientOutOfArea()

    def evacuateDelayed(self):
        print("evacuateDelayed")

        if "military" in self.patient.category:
            self.evacuateMilitaryPatient()
        elif "civilian" in self.patient.category:
            self.evacuateCivilianPatient()

    def evacuateImmediate(self):
        print("evacuateImmediate")

        if "military" in self.patient.category:
            self.evacuateMilitaryPatient()
        elif "civilian" in self.patient.category:
            self.evacuateCivilianPatient()

    def evacuatePatient(self):
        print(f"evacuatePatient patient: {self.patient.id} {self.patient.category} TRIAGE: {self.patient.triage}")

        if "immediate" in self.patient.triage:
            self.evacuateImmediate()
        elif "delayed" in self.patient.triage:
            self.evacuateDelayed()


