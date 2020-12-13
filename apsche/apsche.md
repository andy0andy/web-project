# APScheduler学习使用

**安装**
```shell
pip install apscheduler -i https://pypi.douban.com/simple
```

**基础概念**
APScheduler 具有四种组件:

- triggers（触发器）
    > 触发器管理着 job 的调度方式。
- jobstores （job 存储）
    > 用于 job 数据的持久化。默认 job 存储在内存中，还可以存储在各种数据库中。除了内存方式不需要序列化之外（一个例外是使用 ProcessPoolExecutor），其余都需要 job 函数参数可序列化。另外多个调度器之间绝对不能共享 job 存储（APScheduler 原作者的意思是不支持分布式，但是我们可以通过重写部分函数实现，具体方法后面再介绍）。
- executors （执行器）
    > 负责处理 job。通常使用线程池（默认）或者进程池来运行 job。当 job 完成时，会通知调度器并发出合适的事件。
- schedulers （调度器）
    > 将 job 与以上组件绑定在一起。通常在程序中仅运行一个调度器，并且不直接处理 jobstores ，executors 或 triggers，而是通过调度器提供的接口，比如添加，修改和删除 job。

**组件**
 
```python
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import time
import datetime

# 实例化一个调度器
sche = BlockingScheduler()

# 实验函数
def func(num=10):

    for i in range(num):
        print("i = %d" % i)
        time.sleep(i / 10)

```

1. triggers
    
    1. date: 只在某一时间执行一次
    ```python
    # 在2020-12-12 15:30 运行一次
    sche.add_job(func, "date", run_date=datetime.datetime(2020, 12, 12, 15, 30))
    ```
    2. interval：每个时间间隔执行一次（weeks=0 | days=0 | hours=0 | minutes=0 | seconds=0, start_date=None, end_date=None, timezone=None）
    ```python
    # 每隔10执行一次
    sche.add_job(func, "interval", seconds=10)
    ```
    3. cron：使用linux的crontab方式 (year=None, month=None, day=None, week=None, day_of_week=None, hour=None, minute=None, second=None, start_date=None, end_date=None, timezone=None)
2. executors
    - ThreadPoolExecutor：线程池执行器。
    - ProcessPoolExecutor：进程池执行器。
    - GeventExecutor： Gevent程序执行器。
    - TornadoExecutor： Tornado程序执行器。
    - TwistedExecutor： Twisted程序执行器。
    - AsyncIOExecutor： asyncio程序执行器。
    ```python
    # 配置 default执行器为 ProcessPoolExecutor，并且设置最多的线程数是8个
    execute = {
        "default": ProcessPoolExecutor(8)
    }

    sche = BlockingScheduler(executors=execute)
    ```
3. schedulers
    - BlockingScheduler: 作为独立进程时使用
    - BackgroundScheduler: 在框架程序（如Django、Flask）中使用.
    - AsyncIOScheduler : 当你的程序使用了asyncio的时候使用。

**操作**
```python
job_1 = sche.add_job(func, "interval", seconds=10, id="job_1")

# 开始
sche.start()

# 停止
sche.showdown()

# 删除
job_1.remove()
# or
# sche.remove("job_1)

# 暂停
job_1.pause()
# or
# sche.pause_job("job_1)

# 继续
job_1.resume()
# or
# sche.resume_job("job_1")
```



**综合案例**
> 使用爬虫爬取天气预报，并定时发送到邮箱
