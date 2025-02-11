import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():

    try:
        data = {
            "Guaraní Paraguayo": pd.read_csv('source/archivosCSV/GuaraniParaguayo.csv', sep=','),
            "Peso Argentino": pd.read_csv('source/archivosCSV/PesoArgentino.csv', sep=','),
            "Peso Boliviano": pd.read_csv('source/archivosCSV/PesoBoliviano.csv', sep=','),
            "Peso Chileno": pd.read_csv('source/archivosCSV/PesoChileno.csv', sep=','),
            "Peso Uruguayo": pd.read_csv('source/archivosCSV/PesoUruguayo.csv', sep=','),
            "Real Brasileño": pd.read_csv('source/archivosCSV/RealBrasileño.csv', sep=','),
            "Sol Peruano": pd.read_csv('source/archivosCSV/SolPeruano.csv', sep=',')
        }
        return data
    except Exception as e:
        st.error(f"Error al cargar los datos: {str(e)}")
        return {}
    


def main():

    st.set_page_config(layout="wide")
    
    st.markdown(
    """
    <style>
        div[data-baseweb="select"] > div {
            cursor: pointer !important;
        }
    </style>
    """,
    unsafe_allow_html=True
    )

    
    data = load_data()
    if not data:
        return
    
    monedas = list(data.keys())
    
    st.write("Por favor, selecciona una moneda en la barra lateral (haz clic en '>' Aquí arriba a la izquierda de la pantalla).")
    moneda_seleccionada = st.sidebar.selectbox("Selecciona una moneda para analizar", monedas)
    st.write(f"Moneda seleccionada: {moneda_seleccionada}")
    df1 = data[moneda_seleccionada]
    
    
    if 'Período analizado' in df1.columns and 'Valor de conversión' in df1.columns and 'Período analizado':
        fig = px.line(df1, 
                      x='Período analizado', 
                      y='Valor de conversión', 
                      title='Valor de monedas de Países Sudamericanos en USD ($ En centavos)'
                      
                      )
        fig.update_layout(
                        yaxis=dict(
                            tickformat=",.6f"
                        )
                    )
        
        st.plotly_chart(fig)
    else:
        st.error("Los datos no tienen las columnas esperadas (Fecha y Valor). Verifica el formato de los archivos CSV.")

    st.text('© Renzo Reyna - Data Analyst / Python Developer')

    st.text("CONTACTOS: \n Teléfono: +54 3525 - 620842 (Argentina) \n Email: desarrollador.sarmientino@gmail.com")



if __name__ == "__main__":
    main()
