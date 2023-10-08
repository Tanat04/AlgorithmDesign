def balance_split(goods):
    n = len(goods)
    total_sum = sum(goods)
    print(total_sum, n)
    min_diff = float('inf')

    def split_recursive(index, group_sum):
        print('index, groupsum', index, group_sum)
        nonlocal min_diff
        print('mindiff', min_diff)

        if index == n:
            print(total_sum, group_sum, 2*group_sum)
            diff = abs(total_sum - 2 * group_sum)
            min_diff = min(min_diff, diff)
            print('mindiff', min_diff)
            return

        # Assign the current good to group 0
        split_recursive(index + 1, group_sum + goods[index])
        # Assign the current good to group 1
        split_recursive(index + 1, group_sum)

    split_recursive(0, 0)

    return min_diff


# Test the function
# goods = [5, 8, 13, 27, 14]
goods = list(map(int, input().split()))

minimal_difference = balance_split(goods)
print("Minimal Difference:", minimal_difference)
