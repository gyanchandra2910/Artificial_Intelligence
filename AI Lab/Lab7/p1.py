import copy

initial_domains = {
    '1A': ["TELL", "TENT", "TEST", "SELF", "SAVE", "SORT"],
    '3A': ["SERVE", "SOLVE", "SENSE", "SAVED", "ASSET", "ALERT", "ARIVE", "RINSE", "RIVAL", "RIVER"],
    '5A': ["EGG", "EAR", "EAT"],
    '1D': ["SERVE", "SOLVE", "SENSE", "SAVED", "ASSET", "ALERT", "ARIVE", "RINSE", "RIVAL", "RIVER"],
    '2D': ["SERVE", "SOLVE", "SENSE", "SAVED", "ASSET", "ALERT", "ARIVE", "RINSE", "RIVAL", "RIVER"],
    '4D': ["TELL", "TENT", "TEST", "SELF", "SAVE", "SORT"]
}

arcs = [
    ['1A', 0, '1D', 0], ['1D', 0, '1A', 0],
    ['1A', 2, '2D', 0], ['2D', 0, '1A', 2],
    ['1A', 3, '4D', 0], ['4D', 0, '1A', 3],
    ['3A', 1, '1D', 3], ['1D', 3, '3A', 1],
    ['3A', 3, '2D', 3], ['2D', 3, '3A', 3],
    ['3A', 4, '4D', 3], ['4D', 3, '3A', 4],
    ['5A', 0, '1D', 4], ['1D', 4, '5A', 0],
    ['5A', 2, '2D', 4], ['2D', 4, '5A', 2]
]

box_names = ['1A', '3A', '5A', '1D', '2D', '4D']

def solve_backtrack(assigned_words, current_domains):
    if len(assigned_words) == 6:
        return assigned_words

    khali_box = ""
    for box in box_names:
        if box not in assigned_words:
            khali_box = box
            break

    for word in current_domains[khali_box]:
        word_used = False
        for key in assigned_words:
            if assigned_words[key] == word:
                word_used = True
        
        if word_used:
            continue
            
        word_sahi_hai = True
        for arc in arcs:
            box1 = arc[0]
            idx1 = arc[1]
            box2 = arc[2]
            idx2 = arc[3]
            
            if box1 == khali_box:
                if box2 in assigned_words:
                    if word[idx1] != assigned_words[box2][idx2]:
                        word_sahi_hai = False
                        
        if word_sahi_hai:
            assigned_words[khali_box] = word
            result = solve_backtrack(assigned_words, current_domains)
            if result != None:
                return result
            del assigned_words[khali_box]

    return None

def revise(domains, box_x, idx_x, box_y, idx_y):
    kuch_delete_hua = False
    ache_words_ki_list = []

    for word_x in domains[box_x]:
        sathi_mil_gaya = False
        for word_y in domains[box_y]:
            if word_x[idx_x] == word_y[idx_y]:
                sathi_mil_gaya = True
                break
        
        if sathi_mil_gaya:
            ache_words_ki_list.append(word_x)
        else:
            kuch_delete_hua = True

    domains[box_x] = ache_words_ki_list
    return kuch_delete_hua

def run_ac3(domains):
    queue = []
    for arc in arcs:
        queue.append(arc)

    while len(queue) > 0:
        current_arc = queue.pop(0)
        box1 = current_arc[0]
        idx1 = current_arc[1]
        box2 = current_arc[2]
        idx2 = current_arc[3]

        if revise(domains, box1, idx1, box2, idx2):
            for padosi_arc in arcs:
                if padosi_arc[2] == box1 and padosi_arc[0] != box2:
                    queue.append(padosi_arc)
    return domains

print("BACKTRACKING ")
bt_domains = copy.deepcopy(initial_domains)
bt_solution = solve_backtrack({}, bt_domains)
for box in box_names:
    print(box, "->", bt_solution[box])

print("\nAC-3 ALGORITHM ")
ac3_domains = copy.deepcopy(initial_domains)
ac3_solution = run_ac3(ac3_domains)
for box in box_names:
    print(box, "->", ac3_solution[box])
