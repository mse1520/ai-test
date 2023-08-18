# Python
기본적인 파이썬 사용법 및 프로젝트 설정방법을 설명합니다.
- [파이썬 설치](https://www.python.org/downloads/)


## 기본 명령어
```bash
# app.py 파일을 실행합니다
python ./app.py
```

## venv
프로젝트별로 독립된 가상 환경을 제공합니다. (`npm init` or `gradlew init`과 비슷)
```bash
# 가상환경을 생성합니다 (venv 패키지를 이용해 가상환경 정보인 venv 폴더를 생성)
python -m venv venv
# 가상환경을 활성화 합니다.
./venv/Scripts/activate
# 실행된 가상환경을 비활성화 합니다
deactivate
```

## 윈도우에서 venv
window 환경에서 venv가 실행이 안될 시 파워쉘의 스크립트 실행정책을 변경해야 venv를 사용할 수 있습니다.
```bash
# 현재 파워쉘의 실행 정책을 확인 (기본값은 Restricted)
Get-ExecutionPolicy
# 파워쉘 실행 정책을 'RemoteSigned'으로 변경
Set-ExecutionPolicy RemoteSigned
```

## dependency 파일 만들기(requirements.txt)
- spring 프로젝트에서는 `build.gradle`, node에서는 `package.json`에 해당합니다.
- 파이썬에서는 dependency 정보가 있는 파일을 별도로 명령어를 통해 생성해야합니다.
```bash
# 현재 설치된 패키지 정보를 requirements.txt 파일에 내보냅니다
pip freeze > requirements.txt
# requirements.txt의 정보를 토대로 종속된 패키지를 설치합니다
pip install -r requirements.txt
```