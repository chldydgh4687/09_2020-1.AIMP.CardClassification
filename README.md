# Check_Card_image_classification with Teachable machine

2020-1. SEJONG univ. AI miniproject

[[Youtube_Link]](https://youtu.be/nWOkfHGN6Ck)

<p align="center"><img src="https://github.com/chldydgh4687/2020-1_AI_miniproject/blob/master/git_pic/test_img.PNG" width="100%">

### develop environments
- Teachable_machine_ver.2.0
- Anaconda3
- python 3.7, tensorflow 2.0, keras (crawling_image, augmentation)
- pandas (evaluation)

## Data processing

### google-images_download ([reference](https://github.com/hardikvasa/google-images-download/issues/301#issuecomment-597216052))
- 본프로젝트에서는 네이버에서 크롤링했을 때 잘 나오지않은 카드의 이미지를 크롤링하는데 사용했습니다.
- [how to use google-images_download](https://github.com/chldydgh4687/2020-1_AI_miniproject/issues/1)
```
$cd google-images-download
$python bing_scraper.py --search '비바플래티늄카드' --limit 50 --download --chromedriver ./chromedriver
```
### Naver image Crawling (reference)

- Description  
data 풀더에 카드리스트.txt 만들어서 파이썬코드로 한 줄씩 읽어서 웹상의 이미지를 Naver 풀더에 저장합니다. 리스트별로 풀더가 생성되고 풀더안의 체크카드의 풀더가 또 생성되고 그 안에 그림이 순차적으로 저장됩니다. 

- How to use naver crawling
```
$python cd_img_loader.py
```
### After crawling, Data augmentation 
- 수동적인 작업으로 카드이름과 맞지않은 그림 혹은 augmentation이 과도하게 된 데이터를 삭제합니다.
- 삭제를 했기때문에 부족하고 똑바른 카드가 놓여있는 한가지 경우의 데이터의 양에 대한 과적합을 피하고 학습 성능을 높이기위해서 keras와 다른 툴을 이용하여 회전, 좌우 반전시키거나 잘라주거나, 크기를 조정하거나 명암을 조정합니다.
 
<p align="center"><img src="https://github.com/chldydgh4687/2020-1_AI_miniproject/blob/master/git_pic/e4bae_aug.PNG" width="40%">

</br>

---
# Test with Techable_Machine 
: [https://teachablemachine.withgoogle.com/models/-vbmCVYSx/](https://teachablemachine.withgoogle.com/models/-vbmCVYSx/)
  

<img src="https://github.com/chldydgh4687/2020-1_AI_miniproject/blob/master/git_pic/ANY_0416163500.gif?" width="30%">



## Parameter_Optimization & Evaluation  
### 평가 지표 : Categorical Accuracy [정답(test_solution.csv)/75장의 테스트파일 * 100]
### 평가 방법 : 
```
$python run_evaluation.py
```

### 파라미터 조정과 평가 결과 : 
|epochs|batch_size|learning_Rate|evaluation|
|------|---|---|---|
|50|16|0.001|78.666|
|50|32|0.001|78.666|
|50|32|0.01|66.666|
|100|32|0.001|73.333|
|100|16|0.0005|73.333|

---

### Preprocessed Data
- 학습에 사용했던 데이터  
(Train을 직접 하실 경우, 데이터가 많아서 Train 하고 기다리시거나 응답대기창에서 대기를 5번정도 누르시면 Train 됩니다.)
#### [[Preprocessed_Data_Download_Link]](https://www.dropbox.com/s/46e2ogzl7r9y0cj/NAVER.zip?dl=0) (Naver.zip 157MB)
- 테스트 데이터 75장
#### [[Test_Data_Download_Link]](https://www.dropbox.com/s/eajs98wr59gyeky/test.zip?dl=0) (test.zip 75 file)	
