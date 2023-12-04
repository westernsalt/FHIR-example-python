# FHIR-example-python

한국어로 된 예제 파일들이 적은 것 같아 제가 정리한 파일을 올려둡니다.  
FHIR 개발에 도움되면 좋겠습니다.  

## 프로젝트 소개
파이썬 기반의 Fhir Server와 Client입니다.  
서버는 flask로 구현되어있으며, observation과 patient의 간단한 저장과 검색을 지원합니다.  
필요하다면 다른 리소스를 구현해서 넣을 수 있습니다.  
  
기본적인 통신은 REST API를 사용합니다.  
  
## 설치 방법

### 환경
- Python 3.12.0 이상 권장

### 설치 단계
1. **레포지토리 복제**
   ```bash
   git clone https://github.com/westernsalt/FHIR-example-python.git

2. **의존성 설치**
   ```bash
   pip install -r requirements.txt

### 사용 방법
1. Fhir Server의 실행
   ```bash
   # clone 한 repo의 폴더 내에서
   python fhirServer.py

2. Fhir Client 실행  
Client는 테스트 결과를 보실 수 있도록 주피터 노트북으로 작성했습니다.  
서버를 실행시킨 이후에 순차적으로 Shift + Enter를 활용해 결과를 볼 수 있습니다.  
   

