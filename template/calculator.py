from flask import Flask

app = Flask(__name__)

def template():
    return f'''<!DOCTYPE html> 
    <html>
        <head>
            <meta charset="utf-8">
            <title>내일의창업 수익계산기</title>
            <link rel="icon" type="image/x-icon" href=" ">
            <link rel="stylesheet" href="style.css">
        </head>

        <body style="width:100%; margin:0%">
            <header>
                <div class="topnav">
                    <img class="home" src="https://tmr-founders.com/_next/image?url=%2Fimages%2Flogo%2Flogo.png&w=3840&q=75">
                    <span class="space">
                        <a href="https://tmr-founders.com/story">스토리</a>
                        <a href="https://tmr-founders.com/newsfeed">뉴스피드</a>
                        <a href="https://tmr-founders.com/community">커뮤니티</a>
                        <a href="https://tmr-founders.com/virtual-store">창업하기</a>
                    </span>
                </div>
            </header>

            <div class="block1">
                <div class="result">
                    <h4>예상 월 매출이 1,700만원 일때,</h4>
                    <h3>수익률은 23%
                    <br>월 수익은 약 391만원입니다.</h3>
                </div>

                <ul>
                    <li>  업종별 평균 예상 매출과 지출 비용은 내일의창업이 조사한 내용입니다.</li>
                    <li>  감가상각, 세금(부가가치세·종합소득세), 점주 인건비를 고려하지 않습니다.</li>
                    <li>  실제 창업 조건과 운영 환경에 따라 오차가 발생할 수 있으니 참고용으로 이용해 주세요.</li>
                </ul>
            </div>

            <div class="block2">
                <h2>예상 월 매출</h2>
                <div class="box">
                    <p class="won">1,700만원</p>
                    <!--won class 에 있는 것들은 다 백엔드로 form 입력할때 같이 바뀌게 만들어주세요-->
                    <form name="monthlyProfit" action="" method="post"> <!--post: 정보를 보낸다 / get: 가져온다-->
                        <input class="profit" id="month" type="text" placeholder="예상 월 매출액  ">
                    </form>
                </div>
                <p class="note">커피 업종 평균 월 매출액은 <span class="highlight">1,700만원</span>이예요</p>
                
                <h2>원가</h2>
                    <div class="box">
                        <p class="won">612만원</p>
                        <form name="monthlyProfit" action="" method="post"> <!--post: 정보를 보낸다 / get: 가져온다-->
                            <input class="profit" id="month" type="text" placeholder="식료품  ">
                        </form>
                    </div>
                    <div style="padding-bottom: 1%;"></div>

                    <div class="box">
                        <form>
                            <p class="won">612만원</p>
                            <input class="profit" id="month" type="text" placeholder="소모품  ">
                        </form>
                    </div>
                    <div style="padding-bottom: 1%;"></div>
                    
                    <div class="box">
                        <form>
                            <p class="won">612만원</p>
                            <input class="profit" id="month" type="text" placeholder="기타  ">
                        </form>
                    </div>
                    <p class="note">커피 업종 평균 원가는 매출의 <span class="highlight">36%</span>예요</p>

                <h2>직원 급여</h2>
                    <!-- <span class="option">직접 입력 <span class="text">|</span> 시급으로 계산</span> -->

                    <div class="box">
                        <p class="won">1,700만원</p>
                        <form name="monthlyProfit" action="" method="post"> <!--post: 정보를 보낸다 / get: 가져온다-->
                            <input class="profit" id="month" type="text" placeholder="예상 월 매출액  ">
                        </form>
                    </div>
                    <p class="note">커피 업종 평균 급여는 매출의 <span class="highlight">20%</span>이예요</p>

                <h2>임대료</h2>
                    <div class="box">
                        <p class="won">1,700만원</p>
                        <form name="monthlyProfit" action="" method="post"> <!--post: 정보를 보낸다 / get: 가져온다-->
                            <input class="profit" id="month" type="text" placeholder="임대료  ">
                        </form>
                    </div>
                    <p class="note">커피 업종 평균 임대료는 매출의 <span class="highlight">15%</span>이예요</p>

                <h2>관리비</h2>
                    <div class="box">
                        <p class="won">1,700만원</p>
                        <form name="monthlyProfit" action="" method="post"> <!--post: 정보를 보낸다 / get: 가져온다-->
                            <input class="profit" id="month" type="text" placeholder="관리비  ">
                        </form>
                    </div>
                    <p class="note">커피 업종 평균 관리비는 매출의 <span class="highlight">3%</span>이예요</p>

                <h2>판매 수수료</h2>
                    <div class="box">
                        <p class="won">51만원</p>
                        <form name="monthlyProfit" action="" method="post"> <!--post: 정보를 보낸다 / get: 가져온다-->
                            <input class="profit" id="month" type="text" placeholder="판매 수수료  ">
                        </form>
                    </div>
                    <p class="note">커피 업종 평균 판매 수수료는 매출의 <span class="highlight">3%</span>이예요</p>

                    <div style="margin-bottom:5%"></div>
                    <div>
                        <button class="setting" id="reset">초기화</button> <!--백엔드로 이 버튼 누르면 form input에 다 0 들어가게 해주세요-->
                        <button class="setting" id="average">업종평균</button> <!--백엔드로 이 버튼 누르면 form input에 다 업종 평균값들 들어가게 해주세요-->
                        <button id="calculate">계산하기</button> <!--이 버튼이 눌렸을때 오른쪽 블록이 나타나게 해주세요-->
                    </div>

            </div>

            <!-- <div class="block sticky">
                <div class="result">
                    <h4>예상 월 매출이 1,700만원 일때,</h4>
                    <h3>수익률은 23%
                    <br>월 수익은 약 391만원입니다.</h3>
                </div>

                <ul>
                    <li>  업종별 평균 예상 매출과 지출 비용은 내일의창업이 조사한 내용입니다.</li>
                    <li>  감가상각, 세금(부가가치세·종합소득세), 점주 인건비를 고려하지 않습니다.</li>
                    <li>  실제 창업 조건과 운영 환경에 따라 오차가 발생할 수 있으니 참고용으로 이용해 주세요.</li>
                </ul>
            </div> -->
            
            
        </body>

    </html>
    '''

@app.route('/', methods=['GET', 'POST'])
def count():
    return template()

app.run(debug=True)