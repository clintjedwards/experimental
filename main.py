from datetime import datetime
"""
open all 3 files
parse such that we have the log in a list
count how many lines are in log, level=error count, level=info

TIME FORMAT : 08:56:35.354

top 5 most requested HTTP paths/endpoints
"""

class Logging:
    def __init__(self):
        self.log = []
        self.date_time = []


    def logs(self, file1, file2, file3):
        file_1 = open(file1, 'r')
        file_2 = open(file2, 'r')
        file_3 = open(file3, 'r')

        for line in file_1:
            self.log.append(line)
        for line in file_2:
            self.log.append(line)
        for line in file_3:
            self.log.append(line)

        file_1.close()
        file_2.close()
        file_3.close()

    def get_entry_count(self):
        return len(self.log)

    def get_level_count(self, level):
        count = 0

        for line in self.log:
            if level in line:
                count += 1

        return count

    def log_times(self):
        #TESTCASE: self.date_time.append(datetime.strptime(self.log[0].split("\"", 2)[1], '%Y-%m-%d %H:%M:%S.%f'))

        #DEBUG: for count, val in enumerate(self.log):
            #print(count)
            #print(val.split("\"", 2)[1])

        for i in range(len(self.log)):
            if self.log[0].split("\"", 2)[0] in self.log[i].split("\"", 2)[0]:
                self.date_time.append(datetime.strptime(self.log[i].split("\"", 2)[1], '%Y-%m-%d %H:%M:%S.%f'))

    def get_popular_hour(self):
        self.log_times()
        hour_freq = {}

        for time in self.date_time:
            if time.hour not in hour_freq:
                hour_freq[time.hour] = 1

            hour_freq[time.hour] += 1

        self.date_time = []

        return max(hour_freq, key=hour_freq.get)

    def get_popular_minute(self):
        self.log_times()
        hour_min_freq = {}

        for time in self.date_time:
            if f"{time.hour}:{time.minute}" not in hour_min_freq:
                hour_min_freq[f"{time.hour}:{time.minute}"] = 1

            hour_min_freq[f"{time.hour}:{time.minute}"] += 1

        self.date_time = []

        return max(hour_min_freq, key=hour_min_freq.get)

    def get_top_5_URLs(self):
        #TEST: self.log[0].split(" \\\"")[1].split()
        http_paths = {}

        for line in self.log:
            if "[api" in line:
                if line.split(" \\\"")[1].split()[1] not in http_paths:
                    http_paths[line.split(" \\\"")[1].split()[1]] = 1

                http_paths[line.split(" \\\"")[1].split()[1]] += 1

        return sorted(http_paths, key=http_paths.get, reverse=True)[:5]

    #def get_top_5_endpoints(self):
        """ Not 100% sure what endpoints are. assumption: '/hooks/github/' in https://api.render.com/hooks/github """

def main():
    file1 = 'C:\Files\winprojects\\test\logs\\api-75fd6d7c7d-7qsr5.log'
    file2 = 'C:\Files\winprojects\\test\logs\\api-75fd6d7c7d-brhdl.log'
    file3 = 'C:\Files\winprojects\\test\logs\\api-75fd6d7c7d-nptc9.log'

    main_log = Logging()

    main_log.logs(file1, file2, file3)

    #print(main_log.get_entry_count())
    #print(main_log.get_level_count("level=error"))
    #print(main_log.get_level_count("level=info"))
    #print(main_log.get_popular_hour())
    #print(main_log.get_popular_minute())
    print(main_log.get_top_5_URLs())

main()
