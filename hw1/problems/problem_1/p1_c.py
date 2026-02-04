'''
Problem 1c

input: File containing an integer n followed by 2n lines containing the preferences of the n students and then the n hospitals (see README).
output: Dictionary mapping students to hospitals. 

TODO: Implement the Gale-Shapley algorithm to run in O(n^2).
'''
def stable_matching_1c(file) -> dict:
    n = 0
    doctors_pref = {}
    hospitals_pref = []

    with open(file, "r") as f:
        n = int(f.readline())
        for doctor in range(n): #make doctors_pref into a dictionary of dictionaries to find preference index easier
            d_pref = f.readline().split()
            doctors_pref[doctor] = {int(hospital): int(preference_index) for preference_index, hospital in enumerate(d_pref)}
        for _ in range(n):
            h_pref = f.readline().split()
            fwd_array = [int(x) for x in h_pref]
            hospitals_pref.append(fwd_array[::-1])
    
    # doctors to hospitals map
    pairs = {} 
    matched_hospitals = set()

    while len(matched_hospitals) < n:
        for h in range(n):
            if h not in matched_hospitals:
                doc_preference = hospitals_pref[h].pop() #should now be O(1)

                # If the hospital's preference hasn't been matched
                if doc_preference not in pairs:
                    pairs[doc_preference] = h
                    matched_hospitals.add(h)

                # If the hospital's preference already has a match
                else:
                    h2 = pairs[doc_preference]
                    h1_idx = doctors_pref[doc_preference][h] #now should be O(1)
                    h2_idx = doctors_pref[doc_preference][h2] #now should be O(1)
                    if h1_idx < h2_idx: #fixed by flipping inequality
                        pairs[doc_preference] = h
                        matched_hospitals.add(h)
                        matched_hospitals.remove(h2)

    return pairs

if __name__ == "__main__":
    res = stable_matching_1c("p1d_test.txt")
    print(res)