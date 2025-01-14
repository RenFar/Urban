
import multiprocessing
import time

def read_info(name):
    all_data =[]

    with open(name, "r") as file:
        with open(name, 'r') as file:
            for line in file:
                if line.strip():
                    all_data.append(line)
        return all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейное выполнение
start_time = time.time()
for file_name in filenames:
    data = read_info(file_name)
    print(f"Файл {file_name} прочитан, данных: {len(data)} строк")
end_time = time.time()
linear_time = end_time - start_time
print(f"Время выполнения линейного считывания: {linear_time} секунд")

# Многопроцессное выполнение
#if __name__ == '__main__':
#    start_time = time.time()
#    with multiprocessing.Pool() as pool:
#        processed_data = pool.map(read_info, filenames)
#    end_time = time.time()
#    multiprocessing_time = end_time - start_time
#    print(f"Время выполнения многопроцессного считывания: {multiprocessing_time} секунд")




