# Check_Card_image_classification using teachable machine

2020-1. SEJONG univ. AI miniproject

## Data processing

### google-images_download
- 본프로젝트에서는 네이버에서 크롤링했을 때 잘 나오지않은 카드의 이미지를 크롤링하는데 사용했습니다.
- google-images_download ([reference](https://github.com/hardikvasa/google-images-download/issues/301#issuecomment-597216052))

- [how to use google-images_download](https://github.com/chldydgh4687/2020-1_AI_miniproject/issues/1)
```
$cd google-images-download
$python bing_scraper.py --search 'honeybees' --limit 10 --download --chromedriver /Users/glennjocher/Downloads/chromedriver
```
### Naver image Crawling

- description  
data 풀더에 카드리스트.txt 파일을 생성하여 한 줄씩 읽어서 웹상의 이미지를 긁어와서 Naver 풀더에 리스트별로 풀더가 생성되고 풀더안의 체크카드의 풀더가 또 생성되고 그 안에 그림이 순차적으로 저장됩니다. 

- naver_crawling.py (reference)

- How to use naver crawling
```
$python cd_img_loader.py
```
### After crawling, Data augmentation 
- 수동적인 작업으로 카드이름과 맞지않은 그림을 삭제합니다.
- 삭제를 했기때문에 부족하고 똑바른 카드가 놓여있는 한가지 경우의 데이터의 양의 다양성과 학습 성능을 높이기위해서 keras와 다른 툴을 이용하여 회전, 좌우 반전시키거나 잘라주거나, 크기를 조정하거나 빛의 세기를 조정합니다.

link:[https://nittaku.tistory.com/272](https://nittaku.tistory.com/272)

#### data_augmentation의 방식

-
-
-
-
-

### develop environments
- Teachable_machine_ver.2.0
- python 2.7, pycharm
- android_studio or web
