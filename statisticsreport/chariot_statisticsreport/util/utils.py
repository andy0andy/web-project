import os
import base64
from io import BytesIO



head = '''
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" type="text/css" href="https://www.layuicdn.com/layui/css/layui.css" />
        <title>Report</title>

        <style>
            .report {
                margin-top: 25px;
                margin-bottom: 25px;
            }


            .name {
                margin: 0 45%;
                margin-bottom: 20px;
            }

            .name img {
                width: 40px;
                height: 30px;
            }

            .name p {
                color: #2B6FD5;
                font-size: 25px;
                font-weight: 800;
                vertical-align: middle;
            }

            .nav {
                margin: 0 auto;
                height: 58px;
            }

            .nav div {
                text-align: center;
                height: 100%;
                line-height: 50px;
                background-color: #f2f2f2;
                color: #566573;
                font-weight: 700;
                font-size: 15px;
                cursor: pointer;
            }

            .nav div:hover {
                background-color: #EAECEE ;
                color: black;
            }

            .content div{
                text-align: left;
                height: 100%;
                line-height: 50px;
                color:  #1C2833;
                font-weight: 500;
                font-size: 15px;
                text-indent: 1em;
                cursor: pointer;
                
                border-bottom: #EAECEE  1px solid;
            }

            .content div:hover {
                background-color: #f2f2f2;
            }

            hr {
                background-color: #5FB878;
            }

        </style>
    </head>

    <body>
'''

foot = '''
    </body>

    </html>
'''



def toBytes(func):

    def inner(*args, **kwargs):

        b = BytesIO()

        reports = func(*args, **kwargs)

        b.write(reports.encode())

        return base64.b64encode(b.getvalue()).decode()
    
    return inner




def read_temp(filename):
    # 读取报表模板
    temp_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)

    with open(temp_path) as f:

        return f.read()


@toBytes
def write_temp(reports):

    # 写入报表

    block = '<hr class="layui-container">'.join(reports)

    return head + block + foot






if __name__ == "__main__":
    

    r = '''
        <div class="report layui-container">

            <!-- 报表名 -->
            <div class="name layui-main">
                <img src="https://www.virustotal.com/gui/lit/vt-ui-omnibar/assets/vt_logo.svg" alt="logo">
                <p class="layui-inline">report</p>
            </div>


            <!-- 导航栏 -->
            <div class="nav layui-row layui-col-space5">
                <div class="layui-col-md2">SUMMARY</div>
                <div class="layui-col-md2">DETECTION</div>
                <div class="layui-col-md2">DETAIL</div>
                <div class="layui-col-md2">LINKS</div>
                <div class="layui-col-md2">RELATIONS</div>
                <div class="layui-col-md2">COMMUNITY</div>
            </div>

            <!-- 内容 -->
            <div class="content layui-row layui-col-space5">

                <div class="layui-col-md2">ADMINUSLabs</div>
                <div class="layui-col-md2">AegisLab WebGuard</div>
                <div class="layui-col-md2">AICC (MONITORAPP)</div>
                <div class="layui-col-md2">AlienVault</div>
                <div class="layui-col-md2">Armis</div>
                <div class="layui-col-md2">Artists Against 419</div>
                
                <!-- -- -->

                <div class="layui-col-md2">ADMINUSLabs</div>
                <div class="layui-col-md2">AegisLab WebGuard</div>
                <div class="layui-col-md2">AICC (MONITORAPP)</div>
                <div class="layui-col-md2">AlienVault</div>
                <div class="layui-col-md2">Armis</div>
                <div class="layui-col-md2">Artists Against 419</div>

            </div>

        </div>
    '''


    html = write_temp([r, r])
    print(html)





