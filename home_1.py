import OpenDartReader
import pandas as pd
import FinanceDataReader as fdr
import mplfinance as mpf
import re
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import sys
import datetime

### 0. 객체 생성 ###
# 객체 생성 (API KEY 지정)
api_key = '${API_KEY}'

dart = OpenDartReader(api_key)
df1 = pd.DataFrame()

# 특정기업(삼성전자) 1999년~이후 모든 정기보고서 (최종보고서)
df1 = dart.list('005930', start='2023-01-01', kind='A')
report_idx = df1['rcept_no'][0]
# txt 저장
xml_text = dart.document(report_idx)


# 텍스트 추출 & 전처리 + 텍스트 파일 저장
def extract_refine_text(html_string):
    # Remove CSS styles
    no_css = re.sub('<style.*?</style>', '', html_string, flags=re.DOTALL)

    # Remove Inline CSS
    no_inline_css = re.sub('\..*?{.*?}', '', no_css, flags=re.DOTALL)

    # Remove specific undesired strings
    no_undesired = re.sub('\d{4}[A-Za-z0-9_]*" ADELETETABLE="N">', '', no_inline_css)

    # Remove HTML tags
    no_tags = re.sub('<[^>]+>', ' ', no_undesired)

    # Remove special characters and whitespaces
    cleaned = re.sub('\s+', ' ', no_tags).strip()

    # Remove the □ character
    no_square = re.sub('□', '', cleaned)

    # Replace \' with '
    final_text = re.sub(r"\\'", "'", no_square)

    return final_text


refined_text = extract_refine_text(xml_text)

f = open('삼성전자_사업보고서.txt', 'w')
f.write(str(refined_text))
f.close()

# 아래 두 코드만으로도 주식정보를 가지고 온다.
df_krx = fdr.StockListing('KRX')
df_krx.to_csv('stockList.csv', mode='w', encoding='utf-8-sig')


# 이름으로 코드를 찾기위한 단순한 함수
def codeFromName(name):
    nameList = list(df_krx['Name'])
    return df_krx['Symbol'][nameList.index(name)]


dayBfNum = 1000
strToday = (datetime.datetime.today()).strftime("%Y%m%d")
strFromDay = (datetime.datetime.today() - datetime.timedelta(dayBfNum)).strftime("%Y%m%d")
strShowFromDay = (datetime.datetime.today() - datetime.timedelta(365)).strftime("%Y%m%d")

try:
    # 코드와 기간을 가지고 주식 가격정보를 가지고 올 수 있다니... 너무 편한데?
    # 삼성전자 주가 데이터 가져오기 (2020년 1월 1일부터 현재까지)
    df = fdr.DataReader('005930', '2023-01-01', '2023-08-25')

    # 나는 파일로 저장해서 확인하는게 편하더라.
    # df.to_csv('stockDtlList.csv', mode='w', encoding='utf-8-sig')

    # 이평선 데이터 추가
    ma5 = pd.DataFrame(df['Close'].rolling(window=5).mean())
    ma20 = pd.DataFrame(df['Close'].rolling(window=20).mean())
    ma60 = pd.DataFrame(df['Close'].rolling(window=60).mean())
    ma120 = pd.DataFrame(df['Close'].rolling(window=120).mean())
    ma240 = pd.DataFrame(df['Close'].rolling(window=240).mean())

    df.insert(len(df.columns), '5일', ma5)
    df.insert(len(df.columns), '20일', ma20)
    df.insert(len(df.columns), '60일', ma60)
    df.insert(len(df.columns), '120일', ma120)
    df.insert(len(df.columns), '240일', ma240)

    # 날짜로 필터
    df = df[(df.index >= strShowFromDay)]  # 이평선이 중간부터 표시되는게 싫어서, 앞부분 필터
    chart = df

    DateList = list(df.index)
    VolumeList = list(df['Volume'])
    CloseList = list(df['Close'])

    # 날짜 공백 처리하기
    df_date = pd.to_datetime(DateList)
    # df_date = df_date.strftime(' %m/%d ')

    fig = plt.figure(figsize=(16, 14))
    top_axes = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
    bottom_axes = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)

    top_axes.plot(chart.index, chart['5일'], label='MA5', color='purple', linewidth=1.5)
    top_axes.plot(chart.index, chart['20일'], label='MA20', color='brown', linewidth=1)
    top_axes.plot(chart.index, chart['60일'], label='MA60', color='c', linewidth=1)
    top_axes.plot(chart.index, chart['120일'], label='MA120', color='skyblue', linewidth=1)
    top_axes.plot(chart.index, chart['240일'], label='MA240', color='gold', linewidth=1)
    top_axes.legend(loc="best")

    # top_axes.plot(chart.index,chart['Close'],linewidth= 1)

    top_axes.bar(chart.index, height=chart['Close'] - chart['Open'], bottom=chart['Open'], width=1,
                 color=list(map(lambda c: 'red' if c > 0 else 'blue', chart['Change'])))
    top_axes.vlines(chart.index, chart['Low'], chart['High'],
                    color=list(map(lambda c: 'red' if c > 0 else 'blue', chart['Change'])))

    bottom_axes.bar(df_date, df['Volume'])

    # 파일로 저장하기
    plt.savefig(fname=f'{strToday}_삼성전자.png', bbox_inches='tight', pad_inches=0)

    # 화면에 보여주기
    plt.show()



except:
    print('종목 이름도 모르면 그냥 끝내야지!')
