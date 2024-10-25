import heapq

def decrease_and_conquer(tasks):
    if not tasks:
        return None, None

    if len(tasks) == 1:
        return tasks[0], tasks[0]

    # Maintain two heaps: max_heap for most resources and min_heap for least resources
    max_heap = heapq.nlargest(1, tasks, key=lambda task: task["resources"])
    min_heap = heapq.nsmallest(1, tasks, key=lambda task: task["resources"])

    # Reduce problem size by a constant factor (e.g., half)
    remaining_tasks = tasks[len(tasks) // 2:]

    # Recursively analyze remaining tasks
    max_task, min_task = decrease_and_conquer(remaining_tasks)

    # Compare with current max and min
    if max_task["resources"] >= max_heap[0]["resources"]:
        max_heap[0] = max_task
    if min_task["resources"] <= min_heap[0]["resources"]:
        min_heap[0] = min_task

    return max_heap[0], min_heap[0]

# Example usage
tasks = [
    {"resources": 10},
    {"resources": 5},
    {"resources": 12},
    {"resources": 8},
]

max_task, min_task = decrease_and_conquer(tasks)

print(f"Task with maximum resources: {max_task}")
print(f"Task with minimum resources: {min_task}")
