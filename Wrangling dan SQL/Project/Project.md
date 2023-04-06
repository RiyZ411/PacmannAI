# **Project Wrangling dan SQL**
- Nama    : Riyan Zaenal Arifin
- Email   : riyanzaenal411@gmail.com

## **Import library yang diperlukan**
``` python
import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
```
## **Masukan path file database**
 ``` python
 sqliteConnection = sqlite3.connect('D:/Desktop/Data Science/PacmannAI/Wrangling and SQL/olist.db')
```
## **Melihat table yang ada di database**
``` python
table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", sqliteConnection)
table
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/1.png)
## **Eksplorasi table**
``` python
table = pd.read_sql_query("SELECT * FROM olist_order_customer_dataset;", sqliteConnection)
table
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/2.png)
``` python
table = pd.read_sql_query("SELECT * FROM olist_order_dataset;", sqliteConnection)
table
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/3.png)
``` python
table = pd.read_sql_query("SELECT * FROM olist_order_reviews_dataset;", sqliteConnection)
table
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/4.png)
``` python
table = pd.read_sql_query("SELECT * FROM olist_order_payments_dataset;", sqliteConnection)
table
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/5.png)
``` python
table = pd.read_sql_query("SELECT * FROM olist_order_items_dataset;", sqliteConnection)
table
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/6.png)
``` python
table = pd.read_sql_query("SELECT * FROM olist_products_dataset;", sqliteConnection)
table
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/7.png)
``` python
table = pd.read_sql_query("SELECT * FROM olist_sellers_dataset;", sqliteConnection)
table
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/8.png)
``` python
table = pd.read_sql_query("SELECT * FROM olist_geolocation_dataset;", sqliteConnection)
table
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/9.png)
``` python
table = pd.read_sql_query("SELECT * FROM product_category_name_translation;", sqliteConnection)
table
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/10.png)
## **MENENTUKAN OBJEKTIVE**
Dalam menentukan objektive ini juga dilakukan proses cleaning dan
visaualisasi untuk setiap objektive. Untuk proses data cleaning pada
data data outlier tidak dilakukan karena seluruh objektive menggunakan pengelompokkan bersadarkan masing-masing partisi(menggunakan fungsi group by) untuk mengetahui 
frekuensi kemunculan dari setiap partisi, jika dihilangkan ditakutkan akan
mengurangi informasi terkait frekuensi terendah sehingga ditakutkan
kesalahan dalam mengambil sebuah keputusan

### **1. Perusahaan ingin melihat kategori produk yang paling banyak diorder oleh customer** 
#### **a. Query SQL** 
``` python
objektive1 = pd.read_sql_query(
    "with orderr as(select product_category_name, count(product_id) as jumlah_order from olist_products_dataset inner join olist_order_items_dataset using(product_id) group by product_category_name) select * from orderr order by jumlah_order desc;"
    , sqliteConnection)
objektive1
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/11.png)
#### **b. Data Cleaning** 
##### 1. cek dan hapus missing 
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive1.columns
objektive1[col_names] = objektive1[col_names].replace(missing_values, np.nan)
objektive1.isna().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/12.png)
``` python
objektive1 = objektive1.dropna()
objektive1.isna().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/13.png)
##### 2. cek duplikasi data
``` python
objektive1.duplicated().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/14.png)
##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive1['product_category_name'].unique()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/15.png)
#### **c. Visualization**
``` python
objektive1.plot.bar(x='product_category_name', color="orange")
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/Visualization/93e0be75b6aa06bc124e65d1c66f76ee22be8545.png)
### **2. Perusahaan ingin melihat 15 kategori produk yang memiliki omzet paling tinggi**
``` python
objektive2 = pd.read_sql_query(
    "with omzet as(select product_category_name, sum(price) as banyak_omzet from olist_products_dataset inner join olist_order_items_dataset using(product_id) group by product_category_name) select * from omzet order by banyak_omzet desc limit 15;"
    , sqliteConnection)
objektive2
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/16.png)
#### **b. Data Cleaning**
##### 1. cek dan hapus missing
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive2.columns
objektive2[col_names] = objektive2[col_names].replace(missing_values, np.nan)
objektive2.isna().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/17.png)
##### 2. cek duplikasi data
``` python
objektive2.duplicated().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/18.png)
##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive2['product_category_name'].unique()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/19.png)
#### **c. Visualization** 
``` python
objektive2.plot.bar(x='product_category_name', color="blue")
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/Visualization/75fa2a4342a502a5b1c82e62b960d9cc7e7235c2.png)
### **3. Perusahaan ingin melihat 20 kota teratas yang memiliki jumlah penjualan tertinggi** 
``` python
objektive3 = pd.read_sql_query(
    "SELECT customer_city, customer_state, count(customer_city) as jumlah_penjualan FROM olist_order_customer_dataset inner join olist_order_dataset using(customer_id) join olist_order_items_dataset using(order_id) group by customer_city order by jumlah_penjualan desc limit 20;"
    , sqliteConnection)
objektive3
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/20.png)
#### **b. Data Cleaning** 
##### 1. cek dan hapus missing
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive3.columns
objektive3[col_names] = objektive3[col_names].replace(missing_values, np.nan)
objektive3.isna().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/21.png)
##### 2. cek duplikasi data
``` python
objektive3.duplicated().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/22.png)
##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive3['customer_city'].unique()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/23.png)
``` python
objektive3['customer_state'].unique()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/24.png)
#### **c. Visualization** 
``` python
objektive3.plot.bar(x='customer_city', color="green")
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/Visualization/a3527ba04adc75aed5b794f5983e2eac7dcec790.png)
### **4. Perusahaan ingin melihat jumlah penjualan terbanyak dari 20 kategori produk teratas di kota sao paulo** 
``` python
objektive4 = pd.read_sql_query(
    "with orderl as(select product_category_name, count(order_id) as banyak_order from olist_order_customer_dataset join olist_order_dataset using(customer_id) join olist_order_items_dataset using(order_id) join olist_products_dataset using(product_id) where customer_city = 'sao paulo' group by product_category_name) select * from orderl order by banyak_order desc limit 20;"
    , sqliteConnection)
objektive4
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/25.png)
#### **b. Data Cleaning**
##### 1. cek dan hapus missing 
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive4.columns
objektive4[col_names] = objektive4[col_names].replace(missing_values, np.nan)
objektive4.isna().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/26.png)
``` python
objektive4 = objektive4.dropna()
objektive4.isna().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/27.png)
##### 2. cek duplikasi data 
``` python
objektive4.duplicated().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/28.png)
##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive4['product_category_name'].unique()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/29.png)
#### **c. Visualization**
``` python
objektive4.plot.bar(x='product_category_name', color="red")
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/Visualization/bc857768da9be98d4002571d8d98e8ac5d09364d.png)
### **5. Perusahaan ingin melihat jumlah dari setiap status order di kota sao paulo**
``` python
objektive5 = pd.read_sql_query(
    "with state as(select olist_order_dataset.order_status, customer_city from olist_order_customer_dataset inner join olist_order_dataset using(customer_id)) select order_status, count(customer_city) as jumlah from state where customer_city = 'sao paulo' group by order_status order by jumlah desc;"
    , sqliteConnection)
objektive5
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/30.png)
#### **b. Data Cleaning**
##### 1. cek dan hapus missing 
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive5.columns
objektive5[col_names] = objektive5[col_names].replace(missing_values, np.nan)
objektive5.isna().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/31.png)
##### 2. cek duplikasi data 
``` python
objektive5.duplicated().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/32.png)
##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive5['order_status'].unique()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/33.png)
#### **c. Visualization** 
``` python
objektive5.plot.bar(x='order_status', color="violet")
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/Visualization/3dffa527eba38ad3f6f577a8e3d1d06a2400311c.png)
### **6. Perusahaan ingin melihat jumlah dari tiap metode pembayaran di kota sao paulo** 
``` python
#perusahaan ingin melihat metode pembayaran yang di lakukan oleh customer di kota sao paulo
objektive6 = pd.read_sql_query(
    "with state as(select payment_type, count(olist_order_payments_dataset.payment_type) as jumlah from olist_order_customer_dataset inner join olist_order_dataset using(customer_id) join olist_order_payments_dataset using(order_id) where olist_order_customer_dataset.customer_city = 'sao paulo' group by payment_type) select * from state order by jumlah desc;"
    , sqliteConnection)
objektive6
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/34.png)
#### **b. Data Cleaning** 
##### 1. cek dan hapus missing 
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive6.columns
objektive6[col_names] = objektive6[col_names].replace(missing_values, np.nan)
objektive6.isna().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/35.png)
##### 2. cek duplikasi data
``` python
objektive6.duplicated().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/36.png)
##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive6['payment_type'].unique()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/37.png)
#### **c. Visualization**
``` python
# define Seaborn color palette to use
palette_color = sns.color_palette('bright')[0:10]
  
# plotting data on chart
plt.pie(objektive6['jumlah'], labels=objektive6['payment_type'], colors=palette_color, textprops = {"fontsize":18}, radius = 6.2)
  
# displaying chart
plt.show()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/Visualization/2e4430885cab24e50edbb44b498698760555c2b1.png)
### **7. perusahaan ingin melihat 10 penjual yang menjual barang paling banyak**
``` python
objektive7 = pd.read_sql_query(
    "with seller as(select seller_id, seller_city, seller_state, count(seller_id) as count_sale from olist_sellers_dataset inner join olist_order_items_dataset using(seller_id) group by seller_id) select * from seller order by count_sale desc limit 10;"
    , sqliteConnection)
objektive7
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/38.png)
#### **b. Data Cleaning** 
##### 1. cek dan hapus missing 
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive7.columns
objektive7[col_names] = objektive7[col_names].replace(missing_values, np.nan)
objektive7.isna().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/39.png)
##### 2. cek duplikasi data 
``` python
objektive7.duplicated().sum()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/40.png)
##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive7['seller_city'].unique()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/41.png)
``` python
objektive7['seller_state'].unique()
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/42.png)
#### **c. Visualization** 
``` python
objektive7.plot.bar(x='seller_id', color="black")
```
![table](https://github.com/RiyZ411/Pacmannn/blob/main/Wrangling%20dan%20SQL/Project/Pictures/Visualization/a1aa4310564f62fc4401c8afc7f70f31808596e8.png)
