# %%
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

# st.write("DataFrame")
# df = pd.DataFrame({
#     '1列目':[1, 2, 3, 4, ],
#     '2列目':[10, 20, 30, 40]
# })
# st.write(df)
# st.dataframe(df,width=100,height=100)
# st.dataframe(df.style.highlight_max())
# st.table(df)

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
# st.markdown('Streamlit is **_really_ cool**.')
# st.title('This is a title')
# st.header('This is a header')
# st.subheader('This is a subheader')
# st.text('This is some text.')
# st.caption('This is a string that explains something above.')

# code = '''
# def hello():
#     print("Hello, Streamlit!")
# '''
# st.code(code, language='python')

# st.latex(r'''
#     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
#     ''')


# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c'])

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# map_df = pd.DataFrame(
#     np.random.randn(10, 2)/[500, 500] + [35.56681210714527, 139.6821579335315],
#     columns=("lat", "lon")
# )
# st.map(map_df)

# img = Image.open("canon.png")
# st.image(img, caption="canon logo", use_column_width=True)

# img = Image.open("canon.png")
# # チェックボックス
# if st.checkbox("show Image"):
#     st.image(img, caption="canon logo", use_column_width=True)

# # セレクトボックス
# option = st.selectbox(
#     "あなたが好きな数字を教えてください。",
#     list(range(1, 11))
# )
# st.write("あなたの好きな数字は",option,"です")

# # テキストボックス
# text = st.text_input("あなたの趣味を教えてください")
# "あなたの趣味は",text

# # スライダー
# condition = st.slider("あなたの今の調子は？",0, 100, 50)
# "コンディション：",condition

# サイドバー
# text = st.sidebar.text_input("あなたの趣味を教えてください")
# condition = st.sidebar.slider("あなたの今の調子は？",0, 100, 50)
# "あなたの趣味は",text
# "コンディション：",condition

# 2カラムレイアウト
# left_column, right_column = st.beta_columns(2)
# button = left_column.button("右カラムに文字を表示")
# if button:
#     right_column.write("ここは右カラム")

# プログレスバー
# latest_iteration = st.empty()
latest_iteration = st.text(f'Iteration {1}')
time.sleep(1)
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

# expander
expander = st.expander("問い合わせ1")
expander.text("問い合わせ回答1")
expander.caption("問い合わせ回答1")
expander.caption("問い合わせ回答1")
expander = st.expander("問い合わせ2")
expander.write("問い合わせ回答2")
expander = st.expander("問い合わせ3")
expander.write("問い合わせ回答3")

