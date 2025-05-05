import simpy
import random

# Parameter simulasi
RANDOM_SEED = 42
NUM_CUSTOMERS = 100   # Jumlah pelanggan
NUM_AGENT = 2         # Jumlah loket tiket
INTERARRIVAL_TIME = 2 # Rata-rata waktu antar kedatangan pelanggan (menit)
SERVICE_TIME = 3      # Rata-rata waktu pelayanan di loket (menit)

# Statistik hasil simulasi
waiting_times = []  # Menyimpan waktu tunggu pelanggan
service_times = []  # Menyimpan waktu pelayanan
total_busy_time = 0  # Total waktu semua loket sibuk

class TicketBooth:
    def __init__(self, env, num_agents):
        self.env = env
        self.server = simpy.Resource(env, capacity=num_agents)  # Loket tiket (bisa lebih dari 1)
        self.total_busy_time = 0  # Untuk menghitung utilisasi semua loket

    def serve_customer(self, customer):
        service_duration = random.expovariate(1.0 / SERVICE_TIME)  # Waktu pelayanan acak
        service_times.append(service_duration)
        self.total_busy_time += service_duration
        yield self.env.timeout(service_duration)  # Simulasi waktu pelayanan


def customer(env, name, booth):
    arrival_time = env.now  # Waktu kedatangan pelanggan
    with booth.server.request() as request:
        yield request  # Pelanggan menunggu giliran
        
        waiting_time = env.now - arrival_time  # Hitung waktu tunggu
        waiting_times.append(waiting_time)

        service_duration = random.expovariate(1.0 / SERVICE_TIME)  # Waktu pelayanan acak
        service_times.append(service_duration)
        booth.total_busy_time += service_duration

        print(f"{name} tiba di {arrival_time:.2f} menit, "
              f"menunggu {waiting_time:.2f} menit, "
              f"pelayanan {service_duration:.2f} menit")

        yield env.timeout(service_duration)  # Proses pelayanan


def setup(env, num_customers, booth):
    for i in range(num_customers):
        env.process(customer(env, f"Pelanggan-{i+1}", booth))
        interarrival = random.expovariate(1.0 / INTERARRIVAL_TIME)  # Waktu antar kedatangan acak
        yield env.timeout(interarrival)  # Tunggu sebelum pelanggan berikutnya datang


# Menjalankan simulasi
random.seed(RANDOM_SEED)
env = simpy.Environment()
booth = TicketBooth(env, NUM_AGENT)
env.process(setup(env, NUM_CUSTOMERS, booth))
env.run()

# Analisis hasil
average_waiting_time = sum(waiting_times) / len(waiting_times)
utilization = booth.total_busy_time / (env.now * NUM_AGENT)  # Utilisasi sistem

print("\n===== Hasil Simulasi =====")
print(f"Jumlah Loket: {NUM_AGENT}")
print(f"Rata-rata waktu tunggu: {average_waiting_time:.2f} menit")
print(f"Utilisasi sistem: {utilization:.2%}")
