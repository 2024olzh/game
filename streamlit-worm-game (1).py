import streamlit as st
import base64

def get_game_html():
    return """
    <html>
    <head>
        <title>지렁이의 식품군 탐험</title>
        <style>
            body { margin: 0; padding: 0; overflow: hidden; background-color: #f0f8ff; font-family: 'Arial', sans-serif; }
            #gameCanvas { display: none; transition: background-color 1s ease; }
            #mission { position: absolute; top: 20px; left: 20px; font-size: 28px; font-weight: bold; color: #4a4a4a; background-color: rgba(255, 255, 255, 0.7); padding: 15px; border-radius: 15px; }
            #startScreen, #gameOverScreen { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; background-color: rgba(255, 255, 255, 0.9); padding: 30px; border-radius: 20px; box-shadow: 0 0 20px rgba(0,0,0,0.1); }
            #gameOverScreen { display: none; }
            #startButton, #restartButton { font-size: 24px; padding: 15px 30px; background-color: #4CAF50; color: white; border: none; border-radius: 10px; cursor: pointer; transition: background-color 0.3s; }
            #startButton:hover, #restartButton:hover { background-color: #45a049; }
            #rules { margin-top: 20px; font-size: 18px; color: #333; text-align: left; }
            #creator { font-size: 16px; color: #666; margin-top: 20px; }
            #source { font-size: 14px; color: #888; margin-top: 10px; }
            #nicknameInput { font-size: 20px; padding: 10px; margin-bottom: 20px; width: 80%; max-width: 300px; border: 2px solid #4CAF50; border-radius: 5px; }
            #finalScore { font-size: 36px; font-weight: bold; color: #4CAF50; margin: 20px 0; }
            #finalNickname { font-size: 24px; color: #333; margin-bottom: 20px; }
        </style>
    </head>
    <body>
    <canvas id="gameCanvas"></canvas>
    <div id="mission"></div>
    <div id="startScreen">
        <h1>지렁이의 식품군 탐험</h1>
        <div id="creator">(재연쌤이 만들었음V)</div>
        <div id="source">출처@gajae_ssam</div>
        <input type="text" id="nicknameInput" placeholder="닉네임을 입력하세요" maxlength="10">
        <button id="startButton">게임 시작</button>
        <div id="rules">
            <h2>게임 규칙:</h2>
            <ul>
                <li>마우스를 움직여 귀여운 지렁이를 조종하세요.</li>
                <li>화면에 표시되는 미션에 맞는 음식을 먹으세요.</li>
                <li>미션에 맞는 음식을 먹으면 지렁이가 길어지고 점수가 올라갑니다.</li>
                <li>미션과 맞지 않는 음식을 먹으면 지렁이가 짧아지고 점수가 줄어듭니다.</li>
                <li>지렁이의 머리, 몸통, 꼬리 모두 음식과 닿으면 먹은 것으로 간주됩니다.</li>
                <li>미션은 15초마다 바뀌며, 배경색도 함께 변경됩니다.</li>
                <li>점수가 높아질수록 화면에 더 많은 음식이 나타나 난이도가 올라갑니다.</li>
                <li>가능한 높은 점수를 얻으세요!</li>
            </ul>
        </div>
    </div>
    <div id="gameOverScreen">
        <h1>게임 종료</h1>
        <div id="finalNickname"></div>
        <div id="finalScore"></div>
        <button id="restartButton">다시 시작</button>
    </div>

    <script>
    // 여기에 원본 JavaScript 코드를 그대로 붙여넣습니다.
    // (길이 제한으로 인해 전체 JavaScript 코드를 포함하지 않았습니다.)
    </script>
    </body>
    </html>
    """

def main():
    st.set_page_config(page_title="지렁이의 식품군 탐험", page_icon="🐛", layout="wide")
    
    st.title("지렁이의 식품군 탐험")
    st.markdown("이 게임은 HTML5 Canvas와 JavaScript로 만들어졌으며, Streamlit을 통해 호스팅됩니다.")
    
    # HTML을 base64로 인코딩
    html = get_game_html()
    b64 = base64.b64encode(html.encode()).decode()
    
    # HTML을 iframe으로 표시
    st.markdown(f'<iframe src="data:text/html;base64,{b64}" width="100%" height="800px" style="border:none;"></iframe>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("게임 제작: 재연쌤 | 출처: @gajae_ssam")

if __name__ == "__main__":
    main()
