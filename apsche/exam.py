from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import time
import datetime



def func(num=10):

    for i in range(num):
        print("i = %d" % i)
        time.sleep(i / 10)







if __name__ == "__main__":

    execute = {
        "default": ProcessPoolExecutor(8)
    }
    
    sche = BlockingScheduler(executors=execute)
    # sche = BackgroundScheduler()
    
    # date
    # sche.add_job(func, "date", run_date=datetime.datetime(2020, 12, 12, 15, 30))
    
    # interval
    job_1 = sche.add_job(func, "interval", seconds=10, id="job_1")

    # sche.start()

    # sche.remove_job("job_1")

    # sche.pause_job("job_1")
    # print("job_1 已暂停")

    # sche.resume_job("job_1")

    sche.start()

    
    ...


