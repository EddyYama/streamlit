import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 101')


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問合せ1')
expander.write('回答1')
expander = st.expander('問合せ2')
expander.write('回答2')
expander = st.expander('問合せ3')
expander.write('回答3')

st.write('Progress bar')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)
'Done!!'

# df = pd.DataFrame({
#     '1st': [1, 2, 3, 4],
#     '2nd': [10, 20, 30, 40],
# })
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
# st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=200, height=200) # 動的なテーブルを使いたい時
st.table(df.style.highlight_max(axis=0)) # 静的なテーブルを使いたい時
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df2 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df2)

st.write('Interactive Widgets')

if st.checkbox('Show Image'):
    img = Image.open('IMG20200512123228.jpg')
    st.image(img, caption='LEAF', use_column_width=True)
# 同様にオーディオや動画も簡単に挿入可能

option = st.sidebar.selectbox(
    'あなたが好きな数字を教えてください、',
    list(range(1, 11))
)
text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの好きな数字は', option, 'です'
'あなたの趣味：', text
'あなたの調子：', condition


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
```
"""

