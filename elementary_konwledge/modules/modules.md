datetime模块的时区转换的练习题没有搞明白的代码是
```python

def to_timestamp(dt_str, tz_str):
    dtobj = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz = re.match(r'UTC([+|-]\d{1,}):(\d+)', tz_str).group(1)
    print(tz)
    utc_dt = dtobj.replace(tzinfo=timezone(timedelta(hours=int(tz)))) 
    return utc_dt.timestamp()


    # utc_dt = dtobj.replace(tzinfo=timezone(timedelta(hours=int(tz)))) 
    # 为何能够这样处理时区没看懂


```