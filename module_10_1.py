import time
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, "w") as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Измерение времени выполнения функций
start_time_functions = time.time()

# Вызов функции write_words для каждого файла
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time_functions = time.time()
time_functions = end_time_functions - start_time_functions

# Форматирование времени с помощью strftime
print(f"Работа функций {time.strftime('%H:%M:%S', time.gmtime(time_functions))}")

# Измерение времени выполнения потоков
start_time_threads = time.time()

# Создание потоков
threads = [
    Thread(target=write_words, args=(10, "example5.txt")),
    Thread(target=write_words, args=(30, "example6.txt")),
    Thread(target=write_words, args=(200, "example7.txt")),
    Thread(target=write_words, args=(100, "example8.txt")),
]

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения работы потоков
for thread in threads:
    thread.join()

end_time_threads = time.time()
time_threads = end_time_threads - start_time_threads
print(f"Работа потоков {time.strftime('%H:%M:%S', time.gmtime(time_threads))}")