# Description: FHIR 서버 구현 예시 . hskim

from flask import Flask, request, jsonify
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from fhir.resources.bundle import Bundle
from fhir.resources.bundle import BundleEntry

import json

app = Flask(__name__)

# 간단한 데이터 저장소 (실제 사용 시 데이터베이스 사용)
# 여기서는 환자와 observation만 남겨놨음.
patients = {}
observations = {}

@app.route('/Patient', methods=['POST'])
def CreatePatient():
    data = request.json
    patient = Patient.parse_obj(data)
    id = patient.identifier[0].value
    patients[id] = patient
    print(patient)
    return jsonify({'result': 'Patient created'}), 201

@app.route('/Patient', methods=['GET'])
def GetPatient():
    # 환자 데이터 검색 로직
    # 예시를 위해 하드코딩된 Patient 객체 생성
    patient = None

    id = request.args.get('identifier')
    print(request.args)
    if str(id) in patients:
        patient = patients[id]
        print(patient)

    # Bundle 생성
    bundle = Bundle.construct()
    bundle.type = "searchset"

    # Patient 리소스를 BundleEntry에 추가
    entry = BundleEntry.construct()
    entry.resource = patient
    bundle.entry = [entry]

    # Bundle 객체를 JSON 문자열로 변환
    bundle_json = json.dumps(bundle.json())

    # Bundle 반환
    return json.loads(bundle_json)


@app.route('/Observation', methods=['POST'])
def CreateObservation():
    observation_data = request.json
    observation = Observation.parse_obj(observation_data)

    id = observation.subject.id

    if str(id) not in observations:
        observations[id] = []
        print(id)

    observations[id].append(observation)

    return jsonify({"message": "Observation created successfully", "id": id}), 201

@app.route('/Observation', methods=['GET'])
def GetObservation():
    observation = None

    id = request.args.get('id')
    print(id)

    if str(id) in observations:
        observation = observations[id]
    else:
        return jsonify({"message": "Observation not found"}), 404

    # Bundle 생성
    bundle = Bundle.construct()
    bundle.type = "searchset"
    bundle.entry = []

    # observation 리소스를 BundleEntry에 추가
    for i in range(len(observation)):
        bundle.entry.append({'resource': observation[i]})

    # Bundle 객체를 JSON 문자열로 변환
    bundle_json = json.dumps(bundle.json())

    # Bundle 반환
    return json.loads(bundle_json)

# FHIR 서버 실행
if __name__ == '__main__':
    app.run(debug=True)