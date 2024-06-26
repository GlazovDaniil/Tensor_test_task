def min_substring_for_hash_string(all_nums: tuple[int]) -> int:
    n = len(all_nums)
    x_ = 257
    P = 10 ** 9 + 7
    h = [0] * (n + 1)
    X = [0] * (n + 1)
    X[0] = 1
    all_nums = (0,) + all_nums
    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + all_nums[i]) % P
        X[i] = (X[i - 1] * x_) % P

    end_len = 0
    for length in range(n - 1, 0, -1):
        from2 = n - length
        if (h[length] + h[from2] * X[length]) % P == (h[from2 + length] + h[0] * X[length]) % P:
            end_len = n - length
            break
    if end_len != 0:
        return end_len
    else:
        return n


def min_substring_for_slices(len_tuple: int, all_tuple: tuple[int]) -> int:
    for i in range(1, len_tuple):
        if (len_tuple - 1) % i == 0 and all_tuple[i:] == all_tuple[:-i]:
            return i


def main():
    N = int(input())
    if N > 0:
        nums = tuple(map(int, input().split()))
        # print(min_substring_for_hash_string(nums))  # хеш
        print(min_substring_for_slices(N, nums))  # перебор срезов валидной динны
    else:
        print(0)


if __name__ == '__main__':
    main()
