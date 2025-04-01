import simpy
import random

random.seed(42)  # Ensures reproducibility

arrival_rate = float(input("Enter arrival rate (λ): "))
service_rate = float(input("Enter service rate (μ): "))
num_servers = int(input("Enter number of servers: "))  # Allow dynamic servers

env = simpy.Environment()
server = simpy.Resource(env, num_servers)
log = []

def customer(env, cust_id):
    arrival = env.now
    with server.request() as req:
        yield req
        wait = env.now - arrival
        service_time = random.expovariate(service_rate)
        yield env.timeout(service_time)
        log.append((cust_id, arrival, env.now, wait, service_time))

def generator(env):
    cust_id = 0
    while cust_id < 23:  # Stop generating customers after 25
        yield env.timeout(random.expovariate(arrival_rate))
        cust_id += 1
        env.process(customer(env, cust_id))

env.process(generator(env))
env.run()  # Run until all customers are processed

wait_times = [entry[3] for entry in log]
avg_wait_time = sum(wait_times) / len(wait_times) if wait_times else 0
busy_time = sum(entry[4] for entry in log)
utilization = (busy_time / (num_servers * env.now)) * 100 if env.now > 0 else 0

print("\nCustomer Log:")
print("ID   Arrival  Departure  Wait   Service")
for entry in log:
    print(f"{entry[0]:<4} {entry[1]:<8.2f} {entry[2]:<10.2f} {entry[3]:<6.2f} {entry[4]:.2f}")

print("\nResults:")
print("----------------------------------------")
print(f"Customer Served: {len(log)}")
print(f"Average Wait Time: {avg_wait_time:.2f}")
print(f"Server Utilization: {utilization:.2f}%")
print("----------------------------------------")