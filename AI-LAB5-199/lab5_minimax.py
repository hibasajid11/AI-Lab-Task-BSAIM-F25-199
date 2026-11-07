# Lab 5: Minimax with Leaf Counter
def minimax_counter(depth, index, maximizing, scores, target_depth, counter):
    if depth == target_depth:
        counter[0] += 1
        return scores[index]
    if maximizing:
        val = float('-inf')
        for i in range(2):
            val = max(val, minimax_counter(depth + 1, index * 2 + i, False, scores, target_depth, counter))
        return val
    else:
        val = float('inf')
        for i in range(2):
            val = min(val, minimax_counter(depth + 1, index * 2 + i, True, scores, target_depth, counter))
        return val

scores = [3, 5, 2, 9, 3, 5, 2, 9]
counter = [0]
optimal_val = minimax_counter(0, 0, True, scores, 3, counter)
print(f"Optimal Value: {optimal_val}, Leaves Evaluated: {counter[0]}")