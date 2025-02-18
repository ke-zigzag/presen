import streamlit as st

#関連する単語のリストを定義
words = [
    "トマト", "ノートパソコン", "新聞", "扇風機", "カレンダー",
    "ブドウ", "テレビ", "ホワイトボード", "トラック", "ゴルフクラブ",
    "眼鏡", "スマートフォン", "消しゴム", "サラブレッド", "パスタ",
    "トランプ", "飛行機", "セミ", "自動改札", "スイカ",
    "富士山", "時計", "象", "流れ星", "スクリーン", 
    "氷", "カレー", "マウス", "パンケーキ", "雲",
    "ロックバンド", "信号機", "猿", "UFO","新幹線",
    "サングラス", "カマキリ", "噴水", "ドローン", "唐辛子",
    "ラーメン", "タバコ", "流れるプール", "戦国武将", "キッチンカー",
    "バナナ", "月", "ダウンジャケット", "アイドル", "モーターボート"
]

#状態管理用のセッションステートを初期化
if 'toggle_states' not in st.session_state:
    st.session_state['toggle_states'] = [False] * 50

#タイトル
st.title('50 words memory')

#5×10で表示
num_columns = 10
num_rows = 5

#アクション定義
for i in range(num_rows):
    cols = st.columns(num_columns)
    for j in range(num_columns):
        index = i * num_columns + j
        button_key = f"button_{index}"


        if st.session_state['toggle_states'][index]:
            if cols[j].button(words[index], key=button_key):
                st.session_state['toggle_states'][index] = False
        
        else:
            if cols[j].button(f"{index + 1}", key=button_key):
                st.session_state['toggle_states'][index] = True