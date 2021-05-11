import datetime as dt

def parser(filename):
    with open(filename,'r') as f:
        log_list = f.readlines()
        new_log_list = []
        for log in log_list:
            log = log.split()
            state = log[7]
            time = dt.datetime.strptime(' '.join(log[0:3]), '%b %d %H:%M:%S:%f')
            new_log_list.append((time,state))
        for new_log in new_log_list:





parser('logparser.txt')