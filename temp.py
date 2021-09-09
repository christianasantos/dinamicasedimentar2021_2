

import folium
from folium import IFrame
import base64
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from PIL import Image
from glob import glob

df = pd.read_excel('/Users/admin/Desktop/Cópia de previsão_maré_RJ_2021.xlsx', index_col='Data_Hora')

plt.figure(dpi=3000)
plt.figure(figsize=(40, 25))
plt.plot(df["Altura"])
plt.title('Previsão da Maré - Porto do RJ (Ilha Fiscal) - Setembro de 2021 - Tábua de Marés (CHM)', fontsize=60)

plt.xlabel('Data', fontsize=38)
plt.ylabel('Altura (m)', fontsize=38)
plt.yticks(fontsize=35)
plt.xticks(fontsize=35, rotation='45')
plt.savefig('/Users/admin/Desktop/Fig.png', format='png')

img=Image.open('/Users/admin/Desktop/Fig.png')
width, height=img.size
(new_width, new_height)=((width)/5),((height)/5)
Img=img.resize((round(new_width), round(new_height)), Image.ANTIALIAS)
Img.save('/Users/admin/Desktop/new_Fig.png', format='png')


#Create Map Object
m=folium.Map([-22.5, -43.1669], zoom_start=5)

#Ilha Fiscal
tooltip_IF=('<b>Estação Maregráfica - Ilha Fiscal - RJ</b><br>Latitude: 22.89 S<br>Longitude: 43.17 W<br>Classificação: Mista com dominância Semidiurna')
encoded_IF = base64.b64encode(open('/Users/admin/Desktop/new_Fig.png', 'rb').read()).decode()
html_IF = '<img src="data:image/jpeg;base64,{}">'.format
iframe_IF = folium.IFrame(html_IF(encoded_IF), width=600, height=400)
popup_IF = folium.Popup(iframe_IF, max_width=600)
IF=folium.Marker([-22.8969, -43.1669], popup=popup_IF, tooltip=tooltip_IF).add_to(m)

#Porto Guamaré
tooltip_PG=('<b>Estação Maregráfica - Porto Guamaré - RN</b><br>Latitude: 5.10 S<br>Longitude: 36.32 W<br>Classificação: Semidiurna')
encoded_PG = base64.b64encode(open('/Users/admin/Desktop/PG.png', 'rb').read()).decode()
html_PG = '<img src="data:image/jpeg;base64,{}">'.format
iframe_PG = folium.IFrame(html_PG(encoded_PG), width=600, height=400)
popup_PG = folium.Popup(iframe_PG, max_width=600)
PG=folium.Marker([-5.100833056, -36.3175], popup=popup_PG, tooltip=tooltip_PG).add_to(m)

#Fernando de Noronha
tooltip_FN=('<b>Estação Maregráfica - Fernando de Noronha - PE</b><br>Latitude: 3.83 S<br>Longitude: 32.40 W<br>Classificação: Semidiurna')
encoded_FN = base64.b64encode(open('/Users/admin/Desktop/FN.png', 'rb').read()).decode()
html_FN = '<img src="data:image/jpeg;base64,{}">'.format
iframe_FN = folium.IFrame(html_FN(encoded_FN), width=600, height=400)
popup_FN = folium.Popup(iframe_FN, max_width=600)
FN=folium.Marker([-3.834152778,	-32.40250833], popup=popup_FN, tooltip=tooltip_FN).add_to(m)

#Ilha do Mosqueiro
tooltip_IM=('<b>Estação Maregráfica - Ilha do Mosqueiro - PA</b><br>Latitude: 1.15 S<br>Longitude: 48.47 W<br>Classificação: Semidiurna')
encoded_IM = base64.b64encode(open('/Users/admin/Desktop/IM.png', 'rb').read()).decode()
html_IM = '<img src="data:image/jpeg;base64,{}">'.format
iframe_IM = folium.IFrame(html_IM(encoded_IM), width=600, height=400)
popup_IM = folium.Popup(iframe_IM, max_width=600)
IM=folium.Marker([-1.1525, -48.46805611], popup=popup_IM, tooltip=tooltip_IM).add_to(m)

#Ilha de Trindade
tooltip_IT=('<b>Estação Maregráfica - Ilha de Trindade - ES</b><br>Latitude: 20.51 S<br>Longitude: 29.30 W<br>Classificação: Semidiurna')
encoded_IT = base64.b64encode(open('/Users/admin/Desktop/IT.png', 'rb').read()).decode()
html_IT = '<img src="data:image/jpeg;base64,{}">'.format
iframe_IT = folium.IFrame(html_IT(encoded_IT), width=600, height=400)
popup_IT = folium.Popup(iframe_IT, max_width=600)
IT=folium.Marker([-20.50847222, -29.30166694], popup=popup_IT, tooltip=tooltip_IT).add_to(m)

#Porto de Paranaguá
tooltip_PP=('<b>Estação Maregráfica - Porto de Paranaguá - Cais Oeste - PR</b><br>Latitude: 25.50 S<br>Longitude: 48.52 W<br>Classificação: Semidiurna')
encoded_PP = base64.b64encode(open('/Users/admin/Desktop/PP.png', 'rb').read()).decode()
html_PP = '<img src="data:image/jpeg;base64,{}">'.format
iframe_PP = folium.IFrame(html_PP(encoded_PP), width=600, height=400)
popup_PP = folium.Popup(iframe_PP, max_width=600)
PP=folium.Marker([-25.50027806, -48.51805611], popup=popup_PP, tooltip=tooltip_PP).add_to(m)

#Porto de Florianópolis
tooltip_PF=('<b>Estação Maregráfica - Porto de Florianópolis - SC </b><br>Latitude: 27.58 S<br>Longitude: 48.55 W<br>Classificação: Mista com dominância Semidiurna')
encoded_PF = base64.b64encode(open('/Users/admin/Desktop/PF.png', 'rb').read()).decode()
html_PF = '<img src="data:image/jpeg;base64,{}">'.format
iframe_PF = folium.IFrame(html_PF(encoded_PF), width=600, height=400)
popup_PF = folium.Popup(iframe_PF, max_width=600)
PF=folium.Marker([-27.58416694, -48.55111111], popup=popup_PF, tooltip=tooltip_PF).add_to(m)

#Porto de Salvador
tooltip_PS=('<b>Estação Maregráfica - Porto de Salvador - BA</b><br>Latitude: 12.97 S<br>Longitude: 38.52 W<br>Classificação: Semidiurna')
encoded_PS = base64.b64encode(open('/Users/admin/Desktop/PS.png', 'rb').read()).decode()
html_PS = '<img src="data:image/jpeg;base64,{}">'.format
iframe_PS = folium.IFrame(html_PS(encoded_PS), width=600, height=400)
popup_PS = folium.Popup(iframe_PS, max_width=600)
PS=folium.Marker([-12.96608333, -38.51666667], popup=popup_PS, tooltip=tooltip_PS).add_to(m)

#TEBIG
tooltip_TEBIG=('<b>Estação Maregráfica - Terminal Ilha Guaíba - RJ</b><br>Latitude: 23 S<br>Longitude: 44.03 W<br>Classificação: Mista com dominância Semidiurna')
encoded_TEBIG = base64.b64encode(open('/Users/admin/Desktop/TEBIG.png', 'rb').read()).decode()
html_TEBIG = '<img src="data:image/jpeg;base64,{}">'.format
iframe_TEBIG = folium.IFrame(html_TEBIG(encoded_TEBIG), width=600, height=400)
popup_TEBIG = folium.Popup(iframe_TEBIG, max_width=600)
TEBIG=folium.Marker([-23, -44.03166667], popup=popup_TEBIG, tooltip=tooltip_TEBIG).add_to(m)

#Porto de Tubarão
tooltip_PT=('<b>Estação Maregráfica - Porto de Tubarão - ES</b><br>Latitude: 5.10 S<br>Longitude: 36.32 W<br>Classificação: Semidiurna')
encoded_PT = base64.b64encode(open('/Users/admin/Desktop/PT.png', 'rb').read()).decode()
html_PT = '<img src="data:image/jpeg;base64,{}">'.format
iframe_PT = folium.IFrame(html_PT(encoded_PT), width=600, height=400)
popup_PT = folium.Popup(iframe_PT, max_width=600)
PT=folium.Marker([-20.28416694,	-40.235], popup=popup_PT, tooltip=tooltip_PT).add_to(m)

#Porto de Tutóia
tooltip_PTU=('<b>Estação Maregráfica - Porto de Tutóia - MA</b><br>Latitude: 2.76 S<br>Longitude: 42.275 W<br>Classificação: Semidiurna')
encoded_PTU = base64.b64encode(open('/Users/admin/Desktop/PTU.png', 'rb').read()).decode()
html_PTU = '<img src="data:image/jpeg;base64,{}">'.format
iframe_PTU = folium.IFrame(html_PTU(encoded_PTU), width=600, height=400)
popup_PTU = folium.Popup(iframe_PTU, max_width=600)
PTU=folium.Marker([-2.76275,	-42.275], popup=popup_PTU, tooltip=tooltip_PTU).add_to(m)

#Porto de Cabedelo
tooltip_PC=('<b>Estação Maregráfica - Porto de Cabedelo - PB</b><br>Latitude: 6.98 S<br>Longitude: 34.84 W<br>Classificação: Semidiurna')
encoded_PC = base64.b64encode(open('/Users/admin/Desktop/PC1.png', 'rb').read()).decode()
html_PC = '<img src="data:image/jpeg;base64,{}">'.format
iframe_PC = folium.IFrame(html_PC(encoded_PC), width=600, height=400)
popup_PC = folium.Popup(iframe_PC, max_width=600)
PC=folium.Marker([-6.982833333, -34.84], popup=popup_PC, tooltip=tooltip_PC).add_to(m)

#Porto de Maceió
tooltip_PM=('<b>Estação Maregráfica - Porto de Maceió - AL</b><br>Latitude: 9.69 S<br>Longitude: 35.73 W<br>Classificação: Semidiurna')
encoded_PM = base64.b64encode(open('/Users/admin/Desktop/PM.png', 'rb').read()).decode()
html_PM = '<img src="data:image/jpeg;base64,{}">'.format
iframe_PM = folium.IFrame(html_PM(encoded_PM), width=600, height=400)
popup_PM = folium.Popup(iframe_PM, max_width=600)
PM=folium.Marker([-9.694722222, -35.725], popup=popup_PM, tooltip=tooltip_PM).add_to(m)

m.save("test.html")