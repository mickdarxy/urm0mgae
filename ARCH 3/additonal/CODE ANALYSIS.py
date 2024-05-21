
class TemperatureDataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.temperature_data = []
    # Method to open the file and load lines as an attribute
    def load_data(self):
        with open(self.file_path, 'r') as file:
            data = [line.strip().split() for line in file]
            self.temperature_data = [list(map(int,d[:-1]))+[float(d[len(d)-1])] for d in data]
    # Method to perform the analysis and construct the list
    def construct_temperature_list(self):
        temperature_list = []
        for data in self.temperature_data:
            month, day, year, temperature = data[:]
            if year not in [item[0] for item in temperature_list]:
                temperature_list.append((year, {}))
            if month not in temperature_list[-1][1]:
                temperature_list[-1][1][month] = 0.0
            temperature_list[-1][1][month] = max(temperature , temperature_list[-1][1][month])
        return temperature_list

def main():
    file_path = './temps.txt'
    analyzer = TemperatureDataAnalyzer(file_path)
    analyzer.load_data()
    temperature_list = analyzer.construct_temperature_list()
    print(temperature_list)

if __name__ == '__main__':
    main()
