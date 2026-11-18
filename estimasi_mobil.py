import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    harga_pounds = predict[0]
    harga_idr = harga_pounds * 19000

    # Mengubah pemisah ribuan bawaan (koma) menjadi titik
    format_idr = f"{harga_idr:,.0f}".replace(",", ".")

    st.write('Estimasi harga mobil bekas dalam Ponds : ', round(harga_pounds, 2))
    st.write('Estimasi harga mobil bekas dalam IDR : Rp', format_idr)
