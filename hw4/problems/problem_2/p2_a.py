# Problem 2 a 

def linear_search(packages, boxes):
  ## m x n x b
  ## n packages
  ## m suppliers
  ## b average number of box types offered by each supplier 
  ## boxes = list of list of boxes offered by suppliers
  # len(boxes) = m 

  
  best_waste = float('inf')
  for supplier in boxes:
    waste = 0
    valid = True
    for p in packages:
      best_fit = None
      for b in supplier:
        if b >= p:
          if best_fit is None or b < best_fit:
            best_fit = b
      if best_fit is None:
        valid = False
        break
      waste += best_fit - p

    if valid and waste < best_waste:
      best_waste = waste

  return -1 if best_waste == float('inf') else best_waste