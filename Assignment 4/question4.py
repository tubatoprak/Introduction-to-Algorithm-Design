class Graph:
  def __init__(self):
      self.graph = {}

  def add_edge(self, node1, node2, latency):
      if node1 not in self.graph:
          self.graph[node1] = []
      if node2 not in self.graph:
          self.graph[node2] = []

      self.graph[node1].append((node2, latency))
      self.graph[node2].append((node1, latency))

def exhaustive_search(graph, source, destination, current_path=[], current_latency=0, min_path=None, min_latency=float('inf')):
  current_path = current_path + [source]

  if source == destination:
      if current_latency < min_latency:
          min_path = current_path
          min_latency = current_latency
  else:
      for neighbor, latency in graph[source]:
          if neighbor not in current_path:
              new_latency = current_latency + latency
              new_path = exhaustive_search(graph, neighbor, destination, current_path, new_latency, min_path, min_latency)
              if new_path is not None:
                  min_path, min_latency = new_path, new_latency

  return min_path

# Example usage:
network_graph = Graph()
network_graph.add_edge('A', 'B', 5)
network_graph.add_edge('A', 'C', 3)
network_graph.add_edge('B', 'D', 7)
network_graph.add_edge('C', 'D', 2)
network_graph.add_edge('D', 'E', 4)

source_node = 'A'
destination_node = 'E'

min_path = exhaustive_search(network_graph.graph, source_node, destination_node)
print(f"Minimum latency path from {source_node} to {destination_node}: {min_path}")
