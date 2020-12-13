from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_ERROR

from weather import Weather, sendEmail

sche = BlockingScheduler()




def job():

    weather = Weather()

    info = weather.weatherInfo()

    sendEmail(['1472942893@qq.com'], info)



if __name__ == "__main__":
    
    send_email = sche.add_job(job, "cron", hour="7")

    # sekd_email = sche.add_job(job, "interval", seconds=10)

    sche.start()
