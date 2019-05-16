

# 국가별 박스오피스 기반 영화 추천 & Netflix TV Series 추천



## 0. 팀 정보 및 업무 분담 내역

- 팀명 : I18N
- 강민수 
  - Project Manager
  - 전반적인 서비스 개요 및 흐름 작성
  - django를 활용한 웹 서비스 구축
  - 데이터베이스 모델링
  - template 적용 및 UI customize
  - 각 국가 별 영화 정보 crawler 제작
  - README 초안 작성
- 우상원 
  - Research Assistant
  - PM 보조
  - 데이터베이스 모델링
  - 국가별 영화 정보 제공 사이트 조사
  - README 수정
  - 발표 



## 1. 목표

- 국가별 매주 최신화되는 박스오피스를 제공
- 매월 Netflix의 Top 랭킹을 제공
- HTML/CSS, Javascript, Django, DB 등을 활용한 실제 서비스 설계
- Git을 통한 소스코드 버전 관리 및 협업
- 서비스 배포





## 2. 개발환경

##### 1. Python Web Framework

- Python 3.6.7
- Django 2.1.7

##### 2. Python Library

- `Requirements.txt`

  ```markdown
  beautifulsoup4==4.7.1
  bs4==0.0.1
  certifi==2019.3.9
  chardet==3.0.4
  Django==2.1.7
  django-extensions==2.1.6
  djangorestframework==3.9.3
  idna==2.8
  pytz==2019.1
  requests==2.21.0
  six==1.12.0
  soupsieve==1.9.1
  urllib3==1.24.3
  ```

##### 3. 서비스 배포 환경

- 서버 : Ubuntu
- Database : SQLite



## 3. 서비스 개요

1. 본 서비스는 서비스 방문자의 타 국가의 박스 오피스 순위에 대한 궁금증을 해소하는 것과 해당 국가의 국내 영화 추천을 목적으로  한다.
2. 또한 각 영화의 티저와 관련 정보를 제공함으로써 서비스 방문자가 본 서비스를 이용하는 것으로도 영화에 대한 정보를 취득할 수 있게 만드는 것을 목적으로 한다. 
3. 기존의 서비스(iMDb.com, boxofficemojo.com 등) 들은 다음과 같은 문제점이 존재한다.
   - 해당 국가 별 박스 오피스 정보가 정확하지 않은 경우가 있다.
   - 영미권을 제외하고 정보 업데이트가 느리다.
   - UI/UX가 직관적이지 않고 트렌드에 뒤쳐져있다.
4. 위와 같은 문제점을 해결하고자 본 서비스는 다음과 같은 과정을 거쳤다.
   - 정보가 부정확하기 때문에 해당 국가의 공신력 있는 데이터를 찾아 하나씩 데이터베이스에 추가하였다.
   - 기본적인 영화 정보를 제외하고 모든 것은 수작업으로 진행하였다.
   - UI/UX 측면에서 서비스 방문자가 쉽게 접근할 수 있도록 최신 템플릿을 적용하였다.
   - 모바일 사용자를 위하여 반응형 웹으로 제작하였으며 각종 기기의 페이지뷰에 맞게 UI가 변경된다.
5. 본 서비스가 우선적으로 **주별 박스 오피스**를 조사하고 서비스에 구현한 국가는 다음과 같다.
   - 미국
   - 호주
   - 프랑스
   - 영국
   - 브라질
   - 멕시코
   - 기타 국가 추가 예정
6. 본 서비스는 다양한 국가의 박스 오피스와 별도로 Netflix에 상영중인 TV Series의 **월 별 순위**를 사용자에게 제공한다.
7. 본 서비스상 불필요한 유저 모델은 설정하지 않았다. 





## 4. 서비스 아키텍처 및 제작 과정

##### 1. ERD

![](/Users/dylan/Desktop/github/Movie/ERD.png)



##### 2. Movie Crawler

- IMDB의 [US BoxOffice](https://www.imdb.com/chart/boxoffice) 에서 Box Office를 가져온다.
- [OMDB API](http://www.omdbapi.com/) 를 사용해 각 영화의 상세 정보를 가져온다.
- 영화 Trailer는 크롤링이 불가능해 수동으로 입력한다.



##### 3. Netflix Crawler

- [월 별 Netflix 순위가 개제된 사이트](https://www.techjunkie.com/best-netflix-original-shows/) 에서 TV Series 제목을 가져온다.
- 각 제목을 바탕으로 [Netflix](https://www.netflix.com/) 에서 상세 정보를 가져온다.
- Trailer는 권한 문제로 크롤링이 안되기 때문에 수동으로 youtube에서 링크를 가져온다.



##### 4. 기타 기능

- 관리자 템플릿 뷰 수정

- 관리자 페이에 국가별/장르별 필터링 및 검색 기능 추가

- 방문객들의 영어 실력 증진을 위하여 모든 텍스트는 영어로 작성하였다. 
- 트레일러도 자막 기능을 끈 original 영상이다.
- 본 서비스를 오래 사용할수록 영어 실력이 제고한다.



## 5. 느낀점

- 강민수
  - 암걸렸다. 싸피가 책임져야 한다. 이것도 산재에 포함되는가?
- 우상원
  - 간단한 웹 서비스를 제작 및 배포 하는 것에도 굉장히 다양한 기술과 아이디어가 접목된다는 것을 배웠다. 하나의 완성된 프로젝트는 일반인이 생각하는 예술품과 동일하게 하나의 예술 작품으로써 대접을 해야 한다는 생각을 했다.
