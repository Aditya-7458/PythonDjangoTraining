
arr= [10, 20, 30, 40, 50, 60, 70, 80, 90]
element_to_search = int(input("Enter the element to search: "))

found = False # for optimisation of code
for i in range(len(arr)):
    if arr[i] == element_to_search:
        print(f"Element {element_to_search} found at position {i + 1}.")
        found = True
        break

if not found:
    print(f"Element {element_to_search} not found in the array.")
