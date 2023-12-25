import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#mengimpor data
def get_data():
    return pd.read_csv('air_quality_df.csv')
df = get_data()


#judul data dashboard
st.title('Data Dashboard')
st.subheader('Sumber Data = Air Quality Index (Distrik Shunyi)')

#membuat sidebar untuk control panel yang terdiri dari komponen cuaca dan komponen polutan
with st.sidebar:
    st.title('Control Panel')
    filter_cuaca = st.radio(
        label='Pilih Jenis Komponen Cuaca',
        options=('RAIN','WSPM')
    )
    
    filter_polutan = st.radio(
        label='Pilih Jenis Polutan',
        options = ('PM10','NO2','SO2')
    )


#menampilakn perkembangan dari komponen cuaca di tiap bulannya
st.subheader(f'Perkembangan {filter_cuaca} Tiap Bulannyya')
fig, ax = plt.subplots()
sns.lineplot(x=df['month'], y=df[filter_cuaca], hue=df['year'], palette='Set1')
ax.set_xlabel('Month')
ax.set_ylabel(filter_cuaca)

st.pyplot(fig)

#menampilkan hasil perhitungan korelasi dan penjelasannya.
nilai_korelasi = df[[filter_cuaca,filter_polutan]].corr().iloc[0,1]
pembulatan = round(nilai_korelasi,3)
st.subheader(f'Korelasi antara {filter_cuaca} dan {filter_polutan} adalah sebesar {pembulatan}')

if pembulatan >= 0.7:
    st.subheader(f'{filter_cuaca} dan {filter_polutan} memiliki hubungan positif yang sangat kuat' )
elif pembulatan >= 0.4:
    st.subheader(f'{filter_cuaca} dan {filter_polutan} memiliki hubungan positif yang cukup kuat' )
elif pembulatan >= 0:
    st.subheader(f'{filter_cuaca} dan {filter_polutan} memiliki hubungan positif yang lemah' )
elif pembulatan <= 0:
    st.subheader(f'{filter_cuaca} dan {filter_polutan} memiliki hubungan negatif yang sangat lemah' )
elif pembulatan <= 0.4:
    st.subheader(f'{filter_cuaca} dan {filter_polutan} memiliki hubungan negatif yang lemah' )
else:
    st.subheader(f'{filter_cuaca} dan {filter_polutan} memiliki hubungan negatif yang sangat lemah' )



st.caption('Created by Rizal Aji Santoso')
st.caption('Dicoding ID = rizalajisantos0')

import session_info
session_info.show()
