# Check_Card_Image_Classification with Teachable machine 

2020-1. SEJONG univ. AI miniproject

![https://github.com/chldydgh4687/2020-1_AI_miniproject/blob/master/git_pic/card_recognition.jpg?raw=true](https://github.com/chldydgh4687/2020-1_AI_miniproject/blob/master/git_pic/card_recognition.jpg?raw=true)


### develop environments
- Teachable_machine_ver.2.0
- python 3.7, pycharm, tensorflow 2.0, keras (crawling_image, augmentation)

## Data processing

### google-images_download ([reference](https://github.com/hardikvasa/google-images-download/issues/301#issuecomment-597216052))
- 본프로젝트에서는 네이버에서 크롤링했을 때 잘 나오지않은 카드의 이미지를 크롤링하는데 사용했습니다.
- [how to use google-images_download](https://github.com/chldydgh4687/2020-1_AI_miniproject/issues/1)
```
$cd google-images-download
$python bing_scraper.py --search '비바플래티늄카드' --limit 50 --download --chromedriver ./chromedriver
```
### Naver image Crawling (reference)

- description  
data 풀더에 카드리스트.txt 파일을 생성하여 한 줄씩 읽어서 웹상의 이미지를 긁어와서 Naver 풀더에 리스트별로 풀더가 생성되고 풀더안의 체크카드의 풀더가 또 생성되고 그 안에 그림이 순차적으로 저장됩니다. 

- How to use naver crawling
```
$python cd_img_loader.py
```
### After crawling, Data augmentation 
- 수동적인 작업으로 카드이름과 맞지않은 그림 혹은 augmentation이 과도하게 된 데이터를 삭제합니다.
- 삭제를 했기때문에 부족하고 똑바른 카드가 놓여있는 한가지 경우의 데이터의 양의 다양성과 학습 성능을 높이기위해서 keras와 다른 툴을 이용하여 회전, 좌우 반전시키거나 잘라주거나, 크기를 조정하거나 빛의 세기를 조정합니다.
 
<img src="https://github.com/chldydgh4687/2020-1_AI_miniproject/blob/master/git_pic/e4bae_aug.PNG" width="40%">

</br>

---

## Download_augmentation_Data & Test_Data
#### [[Preprocessed_Data_Download_Link]](https://www.dropbox.com/s/46e2ogzl7r9y0cj/NAVER.zip?dl=0) (Naver.zip 157MB)
#### [[Test_Data_Download_Link]](https://www.dropbox.com/s/eajs98wr59gyeky/test.zip?dl=0) (test.zip 75 file)

## Parameter_Optimization & Evaluation
### 평가 지표 :  정답/75장의 테스트파일 * 100  
  
|epochs|batch_size|learning_Rate|evaluation|
|------|---|---|---|
|50|16|0.001|78.666|
|50|32|0.001|78.666|
|50|32|0.01|66.666|
|100|32|0.001|73.333|
|100|16|0.0005|73.333|

