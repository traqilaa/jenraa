#library
import streamlit as st

#write
st.title('Software Perkalian')
st.subheader('Ini adalah aplikasi untuk mengalikan bilangan bulat')

#input bilangan pertama 
number = st.number_input('Masukkan bilangan pertama')
st.write('Bilangan pertama adalah: ',number)

#input bilangan kedua
number2=st.number_input('Masukkan bilangan kedua')
st.write(f'Bilangan pertama adalah {number2}')

#hasil kali
hasil = number1*number2

if st.button('Hitung'):
    st.write(f'Hasil kali antara {number1} dan {number2} adalah {hasil}')
else 
    st.write('Silahkan penvcet tombol hitung!')
    