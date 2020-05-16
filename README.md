# blog_Wordcloud
## 블로그를 크롤링하여 워드클라우드를 만드는 Text mining
### requirement
- chromedriver(최신버전)
- selenium(3.141.0)
- nltk(3.4.5)
- wordcloud(1.6)
- konlpy(0.5.2)
- matplotlib(3.1.2)
- numpy (1.17.4)
### description
코드는 두개의 단계로 구성되어있습니다. 1. 데이터 수집, 2. 워드클라우드 생성
  #### 1. 데이터수집
  이 단계에서는 chromedriver와 selenium을 이용하여 naver blog에서 입력된 키워드로 검색된 많은 수의 블로그에서 Text를 가져와 수집합니다. 이때 stop_words.txt에 미리 불필요한 단어를 나열하여, 수집 시 해당 단어와 특수기호 같은 불용어는 제거합니다. 수집한 Text는 (키워드).txt 파일에 저장합니다.

  #### 2. Wordcloud 생성 
  저장된 text 데이터를 konlpy에 있는 품사태깅 패키지인 Twitter를 이용하여 명사(Noun)만을 선택합니다. 상위 1000개의 단어만 사용합니다. wordcloud 패키지를 이용하여 이미지를 만드는데 이때 만들고 싶은 wordcloud의 모양을 shape.png로 미리 생성해둬야 합니다. 워드클라우드가 완선되면 (키워드).png 파일로 워드클라우드를 저장합니다.

### 결과 wordcloud
![포항 오도리](https://user-images.githubusercontent.com/28197373/82117633-3c4bef80-97ac-11ea-8f4d-3f6b81309f98.png)
