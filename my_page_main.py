import streamlit as st
import pandas as pd
import numpy as np

st.title('로또 당첨 번호 만들기')

df = pd.DataFrame(np.random.randint(1, 46, size = (5, 6)), columns = ["1번째", "2번째","3번째", "4번째","5번째", "보너스 번호"])

st.write(df)

print("수정 사항~")
