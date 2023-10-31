# Laporan Proyek Machine Learning
### Nama : Vika Fatnawati
### Nim : 211351148
### Kelas : Malam B

## Domain Proyek

Proyek ini dibuat untuk membantu orang yang ingin membeli rumah dan mendapatkan estimasi harga sesuai dengan kondisi rumah dan budget yang mereka miliki

## Business Understanding

Mempermudah mereka yang ingin membeli rumah tanpa harus data ke tempat meskipun hanya melihat dari info di internet terkait kondisi rumah dan cek harga berdasarkan harga pasarannya sehingga mereka bisa mengetahui apakah harga rumah tersebut cocok atau tidak dengan bugdet dan harga pasarannya

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Pembeli rumah harus mencari info harga rumah sesuai pasarannya agar sesuai dengan budget dan kondisi rumah

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Mempermudah pembeli rumah dalam mendapatkan informasi terkait estimasi harga rumah sesuai dengan kondisi rumah dan harga pasarannya

    ### Solution statements
    - Pembuatan Aplikasi yang dapat membantu pembeli rumah dalam mendapatkan informasi terkait estimasi harga rumah tanpa harus datang ke penjual rumah atau menghubungi penjual rumah satu persatu.
    - Model yang dipakai di aplikasi tersebut dibuat menggunakan algoritma Logistic Regression dengan minimal akurasi 70%

## Data Understanding
Dataset yang diambil dari kaggle ini berisi 13 atribut yaitu spesifikasi rumah dan harga rumahnya

Dataset: [Housing Price Prediction](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction/data).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Dataset adalah sebagai berikut:
- price : Harga rumah 
- Area: Luas total rumah dalam kaki persegi.
- Bedrooms: Jumlah kamar tidur di dalam rumah.
- Bathrooms: Jumlah kamar mandi di dalam rumah.
- Stories: Jumlah lantai di dalam rumah.
- Mainroad: Apakah rumah tersebut terhubung dengan jalan utama (Ya/Tidak).
- Guestroom: Apakah rumah tersebut memiliki ruang tamu (Ya/Tidak).
- Basement: Apakah rumah memiliki ruang bawah tanah (Ya/Tidak).
- Hot water heating: Apakah rumah memiliki sistem pemanas air panas (Ya/Tidak).
- Airconditioning: Apakah rumah memiliki sistem pendingin udara (Ya/Tidak).
- Parking: Jumlah tempat parkir yang tersedia di dalam rumah.
- Preferea: Apakah rumah tersebut terletak di area yang disukai (Ya/Tidak).
- Furnishing status: Status perabotan rumah (Fully Furnished, Semi Furnished, Unfurnished).

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

