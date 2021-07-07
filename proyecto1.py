import streamlit as st 
st.title('Mi primera aplicacion')
st.sidebar.title('parametros')
st.header('paso1')
st.write('indicaciones')
a= 2
b= 5 * a 
st.write(b)
import pandas as pd
st.write(1234)
st.write(pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40],}))
#barra de desplazamiento
valor1=st.sidebar.slider('seleccione un valor',0,10,3)
st.checkbox('active el check box',value=False)
st.selectbox('seleccione una opción',('opción 1', 'opción 2', 'opción 3'))
st.multiselect('seleccione una opción',('opción 1', 'opción 2', 'opción 3'))
resultado=valor1 * 10
st.write(resultado)
data1=pd.read_excel('ejemplo.xls',sheet_name='data')
st.write(data1)
data1['nueva columna'] = data1.números * 5
st.write(data1)
from PIL import Image
Imagen1 = Image.open('imagen.jpg')
st.image(Imagen1)
import altair as alt
grafico1 = alt.Chart(data1).mark_point(color = 'red').encode(
	x = 'letras',
	y = 'números',
	color = 'nueva columna',
	tooltip = ['letras','números']).interactive ()
st.altair_chart(grafico1)
import lasio
from io import StringIO
cargar_archivo = st.file_uploader('cargar archivo las',key = None)
if cargar_archivo is None :
	st.write('suba un archivo con extensión las')
if cargar_archivo is not None:
	bites_data = cargar_archivo.read()
	str_io = StringIO(bites_data.decode('Windows-1252'))
	archivo_las = lasio.read(str_io)
	df = archivo_las.df()
	st.write(df)
	df_limpieza = df.dropna(subset = ['NPHI','GR','SP'],axis = 0 , how = 'any')
	st.write(df_limpieza)
l1 = [1, 2, 3, 4, 5]
l2 = ['a','b','c','d','e']
#st.write(l2)
d1 = {'números':l1,'letras':l2}
#st.write(d1)
df1 = pd.DataFrame(d1)
st.write(df1)
i = st.slider('seleccione la profundidad',100,1000,300)
ly = reversed(list(range(-i,0)))
#st.write(ly)
lx = [0] * i
lz = [0] * i
data_xyz = {'eje x':lx, 'eje y':ly, 'eje z':lz}
df2 = pd.DataFrame(data_xyz)
st.write(df2)
import plotly.express as px
figura = px.line_3d(df2, x = 'eje z', y = 'eje x', z = 'eje y')
st.write(figura)