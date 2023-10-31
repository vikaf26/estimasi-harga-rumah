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
    - Model yang dipakai di aplikasi tersebut dibuat menggunakan algoritma Linear Regression dengan minimal akurasi 70%

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

cek null values:
![image](https://github.com/vikaf26/estimasi-harga-rumah/assets/149370346/a8a2c78f-8a51-4c1f-a436-93e1921a8619)

tidak terdapat nilai yang kosong

cek korelasi data:
![image](https://github.com/vikaf26/estimasi-harga-rumah/assets/149370346/a1a0b31d-ff7d-4bb8-a3a0-c808a1e1a089)

cek distribusi harga rumah
![image](https://github.com/vikaf26/estimasi-harga-rumah/assets/149370346/31be87b8-2009-4736-80ec-9fab0621240e)


## Data Preparation
Dikarenakan terdapat tipe data object maka harus kita convert menjadi numerik:
```
enc = LabelEncoder()
df['mainroad'] = enc.fit_transform(df[['mainroad']])
df['guestroom'] = enc.fit_transform(df[['guestroom']])
df['basement'] = enc.fit_transform(df[['basement']])
df['hotwaterheating'] = enc.fit_transform(df[['hotwaterheating']])
df['airconditioning'] = enc.fit_transform(df[['airconditioning']])
df['prefarea'] = enc.fit_transform(df[['prefarea']])
df['furnishingstatus'] = enc.fit_transform(df[['furnishingstatus']])
```

karna data sudah sesuai dengan kebutuhan algoritma maka kita lanjut ke modeling
## Modeling
tahapan pertama yaitu mendeklarasikan X dan Y sebagai atribut dan label:
```
x = df.drop(['price'],axis=1)
y = df['price']
x.shape, y.shape
```
setelah itu menentukan data training dan testing:
```
from sklearn.model_selection import train_test_split
x_train, X_test, y_train, y_test = train_test_split(x,y,random_state=70)
y_test.shape
```
kita scaling dulu datanya:
```
from sklearn.preprocessing import MinMaxScaler
scalar=MinMaxScaler()
x_train=scalar.fit_transform(x_train)
X_test=scalar.fit_transform(X_test)
```
selanjutnya membuat model dengan algoritma linear regression:
```
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
```
```
reg.fit(x_train,y_train)
```

## Evaluation
Pada tahap evaluasi, metrik evaluasi yang dipakai adalah akurasi:
```
score = lr.score(X_test, y_test)
print('akurasi model regresi linier = ', score*100)
```
akurasi model regresi linier =  70.4598411675003

Model yang sudah dibuat dapat dipakai dan di deploy menjadi aplikasi yang dapat dipakai umum dikarenakan mendapatkan akurasi lebih dari 70%.

## Deployment
Model yang sudah dibuat dideploy menggunakan streamlit:
Link aplikasi : [Estimasi Harga Rumah](https://estimasi-harga-rumah.streamlit.app/)

