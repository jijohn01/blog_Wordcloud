# blog_Wordcloud
## 블로그를 크롤링하여 워드클라우드를 만드는 Text mining
### requirement
chromedriver(최신버전)

selenium

nltk

wordcloud

konlpy

matplot

numpy
### description
코드는 두개의 단계로 구성되어있습니다. 1. 데이터 수집, 2. 워드클라우드 생성
#### 1. 데이터수집
이 단계에서는 chromedriver와 selenium을 이용하여 naver blog에서 입력된 키워드로 검색된 많은 수의 블로그에서 Text를 가져와 수집합니다. 이때 stop_words.txt에 미리 불필요한 단어를 나열하여, 수집 시 해당 단어와 특수기호 같은 불용어는 제거합니다. 수집한 Text는 (키워드).txt 파일에 저장합니다.

#### 2. Wordcloud 생성 

