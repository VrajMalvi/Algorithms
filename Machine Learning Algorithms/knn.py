# Should use the `find_k_nearest_neighbors` function below.
import math

def predict_label(examples, features, k, label_key="is_intrusive"):
    # Write your code here.
    knn = find_k_nearest_neighbors(examples, features, k)
    knn_labels = [examples[pid][label_key] for pid in knn]
    return round(sum(knn_labels) / k)


def find_k_nearest_neighbors(examples, features, k):
    # Write your code here.
    distances = {}
    for pid, feature_label_map in  examples.items():
        distance = get_eculidean_distance(features, feature_label_map['features'])
        distances[pid] = distance
    return sorted(distances, key=distances.get)[:k]

def get_eculidean_distance(features, other_features):
    squared_differences = []
    for i in range(len(features)):
        squared_differences.append((other_features[i] - features[i]) ** 2)
    return math.sqrt(sum(squared_differences))