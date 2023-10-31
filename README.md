# Laporan Proyek Machine Learning
### Nama : Vika Fatnawati
### Nim : 211351148
### Kelas : Malam B

## Domain Proyek

Beras sebagai sumber karbohidrat yang banyak dikonsumsi oleh banyak orang. Berbagai macam jenis beras dengan rasa, kegunaan dan cara masak yang berbeda membuat beberapa orang kebingungan dalam membedakan jenis beras tersebut. Dengan rupa yang nyaris sama antara beras, dibuatlah aplikasi yang dapat membantu dalam mengklasifikasi jenis beras

## Business Understanding

Model ini dibuat untuk mempermudah dalam melakukan klasifikasi jenis beras berdasarkan karakteristik dan ciri ukuran beras tersebut.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Sulit nya membedakan antar jenis beras

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Dapat mempermudah dalam membedakan antar jenis beras

    ### Solution statements
    - Pembuatan Aplikasi yang dapat membantu pembeli maupun penjual beras dalam membedakan jenis antar beras berbasis web yang dapat diakses dimana pun dan oleh siapapun
    - Model yang dipakai di aplikasi tersebut dibuat menggunakan algoritma Logistic Regression

## Data Understanding
Dataset yang diambil dari kaggle ini berisi 18185 baris da 12 kolom dengan tipe data keseluruhan numerik

Dataset: [Rice type classification](https://www.kaggle.com/datasets/mssmartypants/rice-type-classification/data).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Dataset adalah sebagai berikut:
- id = Index data ```int64```
- Area = Luas Beras ```int64```
- MajorAxisLength = Panjang Sumbu Utama ```float64```
- MinorAxisLength = Panjang Sumbu Minor ```float64```
- Eccentricity = Eksentrisitas ```float64```
- ConvexArea = Area Cembung ```int64```
- EquivDiameter = Diameter Ekuivalen ```float64```
- Extent = Tingkat Perluasan ```float64```
- Perimeter = Keliling ```float64```
- Roundness = Kebulatan ```float64```
- AspectRation = Aspek Rasio ```float64```
- Class = Jenis Beras (1 = jasmine dan 0 = gonen) ```int64```

## Data Preparation
Sehubung dengan tipe data yang ada didalam dataset sudah sesuai dengan kebutuhan algoritma yang dipakai yaitu full numerik mana preparation yang dilakukan hanyalah penghapusan kolom yang tidak dipakai, yaitu id:
```
df = df.drop(columns = 'id', axis = 1)
```

## Modeling
tahapan pertama yaitu mendeklarasikan X dan Y sebagai atribut dan label:
```
X = df.drop (columns='Class', axis=1)
Y = df['Class']
```
setelah itu menentukan data training dan testing:
```
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, stratify=Y, random_state=2)
```
selanjutnya membuat model dengan algoritma logistic regression:
```
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, Y_train)
```

## Evaluation
Pada tahap evaluasi, metrik evaluasi yang dipakai adalah akurasi:
```
from sklearn.metrics import accuracy_score
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
```
```
print('Akurasi data training adalah = ', training_data_accuracy)
```
Akurasi data training adalah =  0.9891394006048941
```
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
```
```
print('Akurasi data testing adalah = ', test_data_accuracy)
```
Akurasi data testing adalah =  0.9887269727797635

Hasil akhir yang didapatkan adalah akurasi data training sebesar 98% dan testing sebesar 98%.

Model yang sudah dibuat dapat dipakai dan di deploy menjadi aplikasi yang dapat dipakai umum dikarenakan mendapatkan akurasi yang cukup tinggi.

## Deployment
Model yang sudah dibuat dideploy menggunakan streamlit:
Link aplikasi : [Klasifikasi beras](klasifikasi-beras-vika)

