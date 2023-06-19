# Final Project - 충청권 도시 양극화 (2023.05.22 ~)
<br/>

---

[![Blogger](https://img.shields.io/badge/tistory-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://moonstyle1997.tistory.com/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MoonStyIe)
[![Microsoft PowerPoint](https://img.shields.io/badge/portfolio-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)](https://github.com/MoonStyIe/Parkinson/blob/9bed58006a8d646d4058b96eca4f8704263e94c2/pdf/2%EC%A1%B0_%ED%8C%8C%ED%82%A8%EC%8A%A8_%EC%A7%88%EB%B3%91_%EC%A7%84%EB%8B%A8%EC%98%88%EC%B8%A1.pdf)
[![YouTube](https://img.shields.io/badge/presentation-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://youtu.be/XZtytuxL8ws)
[![Mega.nz](https://img.shields.io/badge/Homepage-%23D90007.svg?style=for-the-badge&logo=home-assistant&logoColor=white)](https://github.com/MoonStyIe/Parkinson/blob/e4ea531c446b2dbe079b19ce68930753cfd72afa/img/%ED%99%88%ED%8E%98%EC%9D%B4%EC%A7%80.png)

---

## 💡 목적

충청권 도시에 대해 소득 분포 별 공간 분석 및 지도 시각화, 충청권 도시 양극화 지수 개발, 이에 따른 웹 서비스 구현
<br/>

## 📁 데이터

균형발전지표: <https://www.nabis.go.kr/totalStatisticsDetailView.do?menucd=168> <br/>
충청권 e-지방지표: <https://kostat.go.kr/menu.es?mid=a70501000000> <br/>
NABIS 국가균형발전종합정보시스템: <https://www.nabis.go.kr/> <br/>
인스파일러 데이터 활용 포털: <https://insfiler.com/> <br/>
세종경영자문: <http://sjcounsel.com/> <br/>

## 📊 ERD

<br/>

## 🧑‍🤝‍🧑 팀 구성

<br/>

## 💻 주요 기능

<br/>

## 📥 설치 방법

<br/>

## 📅 주요 기능 업데이트 내용 <br/>
*2023-05-22(월)*
- 대시보드
    + 홈 탭, 조회 탭, EDA 탭 작성
    + 홈 탭의 프로젝트 개요 작성
- PPT
    + 표지 작성
    + 목차 초안 작성

---

*2023-05-23(화)*
- 대시보드
    + 조회 탭의 도별 탭 작성
    + 조회 탭의 시별 탭 작성
    + 수원시 탭의 샘플 지도 작성
- PPT
    + 표지 재작업
    + 목차 완성
    + 상세 목차 작성
    + 프로젝트 개요 작성
    + 팀 역할분담 페이지 작성 및 임시 플롯 차트 완성
- 데이터 수집
    + 나비스(NABIS) 국가균형발전종합정보시스템 데이터 수집
    + 균형지표 관련 데이터 수집
    + 전국 위도·경도 데이터 수집

---

*2023-05-24(수)*
- PPT
    + 목차 재작업
- 데이터 수집
    + 균형발전지표 데이터 수집, 전처리
    + 나비스(NAVIS) 데이터 전처리

---

*2023-05-25(목)*
- 대시보드
    + 데이터 탭 작성
    + 조회 탭 재구성
- PPT
    + 목차 재정비
    + 연구배경 작성
    + 연구목적 작성
    + 선정배경 작성
- 데이터 수집
    + 빅쿼리(BigQuery) 데이터 적재
    + 충청도 데이터 수집
    + 충청지방통계청에서 충청도권 데이터 수집
    + 충남형 양극화 지수 현황판 확인을 위해 충청남도 데이터 담당자에게 전화로 문의
- QGIS
    + 지도구현
- 분석
    + 회귀분석 공부

*2023-05-26(금)*
- 대시보드
    + 조회 탭 재구성
- PPT
    + 목차 재구성
    + 양극화 설명 도식화
    + 충청도 선정 보충설명
- 데이터 수집
    + 빅쿼리(BigQuery) 샘플 데이터 적재
    + 수집한 데이터 통합 및 배포
- QGIS
    + 지도구현
- 분석
    + 지수 개발에 이용할 대영역 소영역 구분
    + 로지스틱 회귀분석 공부
- ERD
    + mapboxgl을 이용한 지도 시각화 연습
    + folium을 이용한 지도 시각화 연습
    + geopandas를 이용한 지도 시각화 연습

---

*2023-05-30(화)*
- 대시보드
    + home 탭 -> 소개 탭 재구성
    + 소개 탭 링크 작성
    + 조회 탭 -> 행정구역별 소득분포 탭 재구성
    + mapboxgl 라이브러리를 이용한 시각화 데이터 업로드 시도했으나, 기능 문제로 실패
- PPT
    + 목차 재구성
    + 임시 웹서비스 소개 탭 작성
    + 개발환경 탭 작성
    + 연구목적 탭 재구성
- 데이터 수집
    + 주택 가격 동향 데이터 수집
    + 점유형태별 데이터 수집
- QGIS
    + 인구 밀도 분석 테스트
- 분석
    + 점유형태별 데이터 정제
    + 복지사업 시군구별 수급권자 현황 데이터 정제
    + 양극화 변수 선택 및 데이터 전처리
- ERD
    + mapboxgl 라이브러리를 이용한 시각화 데이터
    + pydec 라이브러리를 이용한 시각화 데이터
    + folium 라이브러리를 이용한 시각화 데이터

---
