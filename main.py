from typing import List


def maximum_length_of_a_concatenated_string_with_unique_characters(
    arr: List[str],
) -> int:
    arr = [item for item in arr if len(item) == len(set(item))]
    if arr == []:
        return 0
    if len(arr) == 1 and len(set(arr[0])) == len(arr[0]):
        return len(arr[0])
    result = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            ch = ""
            if len(set(arr[i] + arr[j])) == len(arr[i] + arr[j]):
                ch = arr[i] + arr[j]
            result = max(result, len(ch))
    return result


print(
    maximum_length_of_a_concatenated_string_with_unique_characters(
        ["a", "abc", "d", "de", "def"]
    )
)
