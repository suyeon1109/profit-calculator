from flask import Flask, request, redirect

app = Flask(__name__)

def template(contents, monthP=0, returnRate=0, monthRevenue=0):
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
                    <h4>예상 월 매출이 {monthP}원 일때,</h4>
                    <h3>수익률은 {returnRate}%
                    <br>월 수익은 약 {monthRevenue}원입니다.</h3>
                </div>

                <ul>
                    <li>  업종별 평균 예상 매출과 지출 비용은 내일의창업이 조사한 내용입니다.</li>
                    <li>  감가상각, 세금(부가가치세·종합소득세), 점주 인건비를 고려하지 않습니다.</li>
                    <li>  실제 창업 조건과 운영 환경에 따라 오차가 발생할 수 있으니 참고용으로 이용해 주세요.</li>
                </ul>
            </div>

            <div class="block2">
                {contents}
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

def getContents(form1,form2,form3,form4,form5,form6,form7,form8,form9,):
    cnts = f'''
    <h2>예상 월 매출</h2>
    <div class="box">
        <p class="won">1,700만원</p>
        <!--won class 에 있는 것들은 다 백엔드로 form 입력할때 같이 바뀌게 만들어주세요-->
        {form1}
    </div>
    <p class="note">커피 업종 평균 월 매출액은 <span class="highlight">1,700만원</span>이예요</p>
    
    <h2>원가</h2>
        <div class="box">
            <p class="won">612만원</p>
            {form2}
        </div>
        <div style="padding-bottom: 1%;"></div>

        <div class="box">
            <p class="won">612만원</p>
            {form3}
        </div>
        <div style="padding-bottom: 1%;"></div>
        
        <div class="box">
            <p class="won">612만원</p>
            {form4}
        </div>
        <p class="note">커피 업종 평균 원가는 매출의 <span class="highlight">36%</span>예요</p>

    <h2>직원 급여</h2>
        <!-- <span class="option">직접 입력 <span class="text">|</span> 시급으로 계산</span> -->

        <div class="box">
            <p class="won">1,700만원</p>
            {form5}
        </div>
        <p class="note">커피 업종 평균 급여는 매출의 <span class="highlight">20%</span>이예요</p>

    <h2>임대료</h2>
        <div class="box">
            <p class="won">1,700만원</p>
            {form6}
        </div>
        <p class="note">커피 업종 평균 임대료는 매출의 <span class="highlight">15%</span>이예요</p>

    <h2>관리비</h2>
        <div class="box">
            <p class="won">1,700만원</p>
            {form7}
        </div>
        <p class="note">커피 업종 평균 관리비는 매출의 <span class="highlight">3%</span>이예요</p>

    <h2>판매 수수료</h2>
        <div class="box">
            <p class="won">51만원</p>
            {form8}
        </div>
        <p class="note">커피 업종 평균 판매 수수료는 매출의 <span class="highlight">3%</span>이예요</p>

        <div style="margin-bottom:5%"></div>
        <div>
            {form9}
        </div>
    '''
    return cnts



@app.route('/', methods=['GET', 'POST'])
def count():
    if request.method == 'GET':
        content1 = '''
        <form name="monthlyProfit" action="" method="post"> <!--post: 정보를 보낸다 / get: 가져온다-->
            <input class="profit" id="month" type="text" placeholder="예상 월 매출액" name="monthP">
        </form>
        '''
        content2 = '''
        <form name="monthlyProfit" action="" method="post"> 
            <input class="profit" id="month" type="text" placeholder="식료품" name="cost1">
        </form>
        '''
        content3 = '''
        <form>
            <input class="profit" id="month" type="text" placeholder="소모품" name="cost2">
        </form>
        '''
        content4 = '''
        <form>
            <input class="profit" id="month" type="text" placeholder="기타" name="cost3">
        </form>
        '''
        content5 = '''
        <form name="monthlyProfit" action="" method="post"> 
            <input class="profit" id="month" type="text" placeholder="예상 월 매출액" name="pay">
        </form>
        '''
        content6 = '''
        <form name="monthlyProfit" action="" method="post"> <!--post: 정보를 보낸다 / get: 가져온다-->
            <input class="profit" id="month" type="text" placeholder="임대료" name="rent">
        </form>
        '''
        content7 = '''
        <form name="monthlyProfit" action="" method="post"> 
            <input class="profit" id="month" type="text" placeholder="관리비" name="manage">
        </form>
        '''
        content8 = '''
        <form name="monthlyProfit" action="" method="post"> 
            <input class="profit" id="month" type="text" placeholder="판매 수수료" name="fees">
        </form>
        '''
        content9 = '''
        <form action="" method="POST">
            <input class="setting" id="reset" type="submit" value="초기화"></input> <!--백엔드로 이 버튼 누르면 form input에 다 0 들어가게 해주세요-->
            <input class="setting" id="average" type="submit" value="업종평균"></input> <!--백엔드로 이 버튼 누르면 form input에 다 업종 평균값들 들어가게 해주세요-->
            <input id="calculate" type="submit" value="계산하기"></input> <!--이 버튼이 눌렸을때 오른쪽 블록이 나타나게 해주세요-->
        </form>
        '''
        return template(getContents(content1,content2,content3,content4,content5,content6,content7,content8,content9))
    elif request.method == 'POST':
        monthP = int(request.form['monthP'])
        cost1 = int(request.form['cost1'])
        cost2 = int(request.form['cost2'])
        cost3 = int(request.form['cost3'])
        pay = int(request.form['pay'])
        rent = int(request.form['rent'])
        manage = int(request.form['manage'])
        fees = int(request.form(['fees']))
        revenue = monthP - sum(cost1, cost2, cost3, pay, rent, manage, fees)
        return template(getContents(),monthP, revenue, round(revenue*100/monthP, 1))




app.run(debug=True)