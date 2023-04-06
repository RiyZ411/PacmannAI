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

``` python
table = pd.read_sql_query("SELECT * FROM olist_order_dataset;", sqliteConnection)
table
```

``` python
table = pd.read_sql_query("SELECT * FROM olist_order_reviews_dataset;", sqliteConnection)
table
```

``` python
table = pd.read_sql_query("SELECT * FROM olist_order_payments_dataset;", sqliteConnection)
table
```

``` python
table = pd.read_sql_query("SELECT * FROM olist_order_items_dataset;", sqliteConnection)
table
```

``` python
table = pd.read_sql_query("SELECT * FROM olist_products_dataset;", sqliteConnection)
table
```

``` python
table = pd.read_sql_query("SELECT * FROM olist_sellers_dataset;", sqliteConnection)
table
```

``` python
table = pd.read_sql_query("SELECT * FROM olist_geolocation_dataset;", sqliteConnection)
table
```

``` python
table = pd.read_sql_query("SELECT * FROM product_category_name_translation;", sqliteConnection)
table
```

## **MENENTUKAN OBJEKTIVE**
Dalam menentukan objektive ini juga dilakukan proses cleaning dan
visaualisasi untuk setiap objektive. Untuk proses data cleaning pada
data data outlier tidak dilakukan karena seluruh objektive menggunakan
frekuensi kemunculan dari sebuah data, jika dihilangkan ditakutkan akan
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

#### **b. Data Cleaning** 
##### 1. cek dan hapus missing 
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive1.columns
objektive1[col_names] = objektive1[col_names].replace(missing_values, np.nan)
objektive1.isna().sum()
```

``` python
objektive1 = objektive1.dropna()
objektive1.isna().sum()
```

##### 2. cek duplikasi data
``` python
objektive1.duplicated().sum()
```

##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive1['product_category_name'].unique()
```

#### **c. Visualization**
``` python
objektive1.plot.bar(x='product_category_name', color="orange")
```

### **2. Perusahaan ingin melihat 15 kategori produk yang memiliki omzet paling tinggi**
``` python
objektive2 = pd.read_sql_query(
    "with omzet as(select product_category_name, sum(price) as banyak_omzet from olist_products_dataset inner join olist_order_items_dataset using(product_id) group by product_category_name) select * from omzet order by banyak_omzet desc limit 15;"
    , sqliteConnection)
objektive2
```

#### **b. Data Cleaning**
##### 1. cek dan hapus missing
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive2.columns
objektive2[col_names] = objektive2[col_names].replace(missing_values, np.nan)
objektive2.isna().sum()
```

``` python
objektive2 = objektive2.dropna()
objektive2.isna().sum()
```

##### 2. cek duplikasi data
``` python
objektive2.duplicated().sum()
```

##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive2['product_category_name'].unique()
```

#### **c. Visualization** {#c-visualization}
``` python
objektive2.plot.bar(x='product_category_name', color="blue")
```

### **3. Perusahaan ingin melihat 20 kota teratas yang memiliki jumlah penjualan tertinggi** 
``` python
objektive3 = pd.read_sql_query(
    "SELECT customer_city, customer_state, count(customer_city) as jumlah_penjualan FROM olist_order_customer_dataset inner join olist_order_dataset using(customer_id) join olist_order_items_dataset using(order_id) group by customer_city order by jumlah_penjualan desc limit 20;"
    , sqliteConnection)
objektive3
```

#### **b. Data Cleaning** 
##### 1. cek dan hapus missing
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive3.columns
objektive3[col_names] = objektive3[col_names].replace(missing_values, np.nan)
objektive3.isna().sum()
```

``` python
objektive3 = objektive3.dropna()
objektive3.isna().sum()
```

##### 2. cek duplikasi data
``` python
objektive3.duplicated().sum()
```

##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive3['customer_city'].unique()
```

``` python
objektive3['customer_state'].unique()
```

#### **c. Visualization** 
``` python
objektive3.plot.bar(x='customer_city', color="green")
```

### **4. Perusahaan ingin melihat jumlah penjualan terbanyak dari 20 kategori produk teratas di kota sao paulo** 
``` python
objektive4 = pd.read_sql_query(
    "with orderl as(select product_category_name, count(order_id) as banyak_order from olist_order_customer_dataset join olist_order_dataset using(customer_id) join olist_order_items_dataset using(order_id) join olist_products_dataset using(product_id) where customer_city = 'sao paulo' group by product_category_name) select * from orderl order by banyak_order desc limit 20;"
    , sqliteConnection)
objektive4
```

#### **b. Data Cleaning**
##### 1. cek dan hapus missing 
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive4.columns
objektive4[col_names] = objektive4[col_names].replace(missing_values, np.nan)
objektive4.isna().sum()
```

``` python
objektive4 = objektive4.dropna()
objektive4.isna().sum()
```

##### 2. cek duplikasi data 
``` python
objektive4.duplicated().sum()
```

##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive4['product_category_name'].unique()
```

#### **c. Visualization**
``` python
objektive4.plot.bar(x='product_category_name', color="red")
```

### **5. Perusahaan ingin melihat jumlah dari setiap status order di kota sao paulo**
``` python
objektive5 = pd.read_sql_query(
    "with state as(select olist_order_dataset.order_status, customer_city from olist_order_customer_dataset inner join olist_order_dataset using(customer_id)) select order_status, count(customer_city) as jumlah from state where customer_city = 'sao paulo' group by order_status order by jumlah desc;"
    , sqliteConnection)
objektive5
```

#### **b. Data Cleaning**
##### 1. cek dan hapus missing 
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive5.columns
objektive5[col_names] = objektive5[col_names].replace(missing_values, np.nan)
objektive5.isna().sum()
```

``` python
objektive5 = objektive5.dropna()
objektive5.isna().sum()
```

##### 2. cek duplikasi data 
``` python
objektive5.duplicated().sum()
```

##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive5['order_status'].unique()
```

#### **c. Visualization** {#c-visualization}
``` python
objektive5.plot.bar(x='order_status', color="violet")
```

### **6. Perusahaan ingin melihat jumlah dari tiap metode pembayaran di kota sao paulo** 
``` python
#perusahaan ingin melihat metode pembayaran yang di lakukan oleh customer di kota sao paulo
objektive6 = pd.read_sql_query(
    "with state as(select payment_type, count(olist_order_payments_dataset.payment_type) as jumlah from olist_order_customer_dataset inner join olist_order_dataset using(customer_id) join olist_order_payments_dataset using(order_id) where olist_order_customer_dataset.customer_city = 'sao paulo' group by payment_type) select * from state order by jumlah desc;"
    , sqliteConnection)
objektive6
```

#### **b. Data Cleaning** 
##### 1. cek dan hapus missing 
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive6.columns
objektive6[col_names] = objektive6[col_names].replace(missing_values, np.nan)
objektive6.isna().sum()
```

``` python
objektive6 = objektive6.dropna()
objektive6.isna().sum()
```

##### 2. cek duplikasi data
``` python
objektive6.duplicated().sum()
```

##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive6['payment_type'].unique()
```

#### **c. Visualization** {#c-visualization}
``` python
# define Seaborn color palette to use
palette_color = sns.color_palette('bright')[0:10]
  
# plotting data on chart
plt.pie(objektive6['jumlah'], labels=objektive6['payment_type'], colors=palette_color, textprops = {"fontsize":18}, radius = 6.2)
  
# displaying chart
plt.show()
```

### **7. perusahaan ingin melihat 10 penjual yang menjual barang paling banyak**
``` python
objektive7 = pd.read_sql_query(
    "with seller as(select seller_id, seller_city, seller_state, count(seller_id) as count_sale from olist_sellers_dataset inner join olist_order_items_dataset using(seller_id) group by seller_id) select * from seller order by count_sale desc limit 10;"
    , sqliteConnection)
objektive7
```

#### **b. Data Cleaning** 
##### 1. cek dan hapus missing 
``` python
missing_values = ["", " ", "None", "none"] #definisikan nilai missing yang mungkin terjadi
col_names = objektive7.columns
objektive7[col_names] = objektive7[col_names].replace(missing_values, np.nan)
objektive7.isna().sum()
```

``` python
objektive7 = objektive7.dropna()
objektive7.isna().sum()
```

##### 2. cek duplikasi data 
``` python
objektive7.duplicated().sum()
```

##### 3. Cek inkonsisten format atau tipe daya
``` python
objektive7['seller_city'].unique()
```

``` python
objektive7['seller_state'].unique()
```

#### **c. Visualization** 
``` python
objektive7.plot.bar(x='seller_id', color="black")
```

