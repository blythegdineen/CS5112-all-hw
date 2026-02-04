
def binary_search(packages, boxes):
    # packages: integer array of all distinct sizes
    # m x log(n) x b
    ## n packages --> binary search over n 
    ## m suppliers --> for loop
    ## b boxes from supplier --> for loop
  
    best_waste = float('inf')
    packages = sorted(packages)
    for supplier in boxes:
        waste = 0
        remaining = packages[:]
        supplier = sorted(supplier)
        for b in supplier:
            left = 0
            right = len(remaining) - 1
            package_index = -1
            while left <= right:
                mid = (left+right) //2
                if remaining[mid] <= b:
                    package_index = mid
                    left = mid +1
                else:
                    right = mid - 1
            if package_index != -1:
                for r in range(package_index+1):
                    waste += (b - remaining[r])
                remaining = remaining[(package_index+1):]
        if len(remaining) ==0 and waste < best_waste:
            best_waste = waste
    return -1 if best_waste == float('inf') else best_waste

