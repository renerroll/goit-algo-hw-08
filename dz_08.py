import heapq

def minimize_cost(cables):
    heap = cables[:]
    heapq.heapify(heap)
    total_cost = 0
    connections = []

    while len(heap) > 1:
        # Витягуємо два кабелі з найменшою довжиною
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)
        # Об'єднуємо їх
        merged_cable = (cable1[0] + cable2[0], f"({cable1[1]} + {cable2[1]})")
        # Додаємо новий об'єднаний кабель назад до купи
        heapq.heappush(heap, merged_cable)
        # Додаємо витрати на об'єднання до загальних витрат
        total_cost += merged_cable[0]
        # Записуємо з'єднання
        connections.append((cable1[1], cable2[1]))

    return total_cost, connections

if __name__ == "__main__":
    cables = [(10, 'A'), (11, 'B'), (3, 'C'), (6, 'D'), (3, 'E')]
    total_cost, connections = minimize_cost(cables)
    print(f"Сумарні витрати: {total_cost}")
    print("Порядковість об'єднання:")
    for connection in connections:
        print(f"{connection[0]} => {connection[1]}")
