import time

class olahData:
    def __init__(self, data):
        self.data = data
    def readData(self):
        print(f'[1] Read data ke : {self.data}')
        time.sleep(2)
    def sortData(self):
        print(f'[2] Sort Data ke : {self.data}')
        time.sleep(2)
    def exportData(self):
        print(f'[3] Export data ke : {self.data}')
        time.sleep(1)
    def run(self):
        self.readData()
        self.sortData()
        self.exportData()

if __name__ == '__main__':
    start = time.perf_counter()
    datas = [
        '1-100000',
        '100001-200000',
        '200001-300000',
        '300001-400000',
        '400001-500000',
         ]
    for data in datas :
        olahData(data).run()
    finish = time.perf_counter()
    print('waktu total :', finish-start)