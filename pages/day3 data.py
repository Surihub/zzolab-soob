import streamlit as st
import requests
import json
from mymodule.module1 import grid
import folium
from folium.plugins import Draw
from streamlit_folium import st_folium, folium_static

st.title("실시간 날씨 확인하기!")

st.subheader("아래 지도에서 원하는 지점을 마우스로 클릭해보세요.")
m = folium.Map(location=[37.49, 127.15], zoom_start=10)
Draw(export=True).add_to(m)

output = st_folium(m, width=500, height=300)
# st.write(output)

point_lat = output['last_clicked']['lat']
point_lng = output['last_clicked']['lng']

st.write(point_lat, point_lng)
# point_lat = 37.1124124124
# point_lng = 127.235

nx, ny = grid(point_lat, point_lng)

# nx = '62'
# ny = '129'
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : st.secrets['datagokr']['key'],
          'pageNo' : '1',
          'numOfRows' : '100',
          'dataType' : 'JSON', 
          'base_date' : '20231122',
          'base_time' : '0600',
          'nx' : nx, 'ny' : ny }
response = requests.get(url, params=params)
# st.write(response.content)

json_data = json.loads(response.content.decode('utf-8'))
# st.write(json_data)

result_dict = {}
for item in json_data['response']['body']['items']['item']:
    category = item['category']
    obsrValue = item['obsrValue']
    result_dict[category] = obsrValue


# 영문 키와 한글 키의 매핑 딕셔너리
key_mapping = {
    'T1H': '기온(℃)',
    'RN1': '1시간 강수량(mm)',
    'UUU': '동서바람성분(m/s)',
    'VVV': '남북바람성분(m/s)',
    'REH': '습도(%)',
    'PTY': '강수형태',
    'VEC': '풍향(deg)',
    'WSD': '풍속(m/s)'
}

# 새로운 딕셔너리 생성 및 키 변경
new_dict = {key_mapping[key]: value for key, value in result_dict.items()}

# 결과 딕셔너리 출력
st.table(new_dict)