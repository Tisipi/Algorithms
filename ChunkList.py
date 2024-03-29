def chunk_list(list, chunk_size):
    """
    Chunks a list in a list of equal-sized lists of size chunk_size
    """
    if list == []:
        return list

    # validate_input(list, chunk_size)
    chunks = []
    chunks.append(list[0:chunk_size])
    chunks.extend(chunk_list(list[chunk_size:], chunk_size))
    return chunks


def validate_input(list, chunk_size):
    # if not isinstance(list, list):
    #     raise ValueError("Not a list")
    if chunk_size <= 0:
        raise ValueError("Invalid chunk size. Chunk size must be >=1")
    elif chunk_size > len(list):
        raise ValueError(
            "Invalid chunk size. Chunk size must be smaller then list length"
        )


if __name__ == "__main__":
    print(chunk_list([], 1))
    print(chunk_list([1, 2, 3, 4], 1))
    print(chunk_list([1, 2, 3, 4], 2))
    # print(chunk_list([1, 2, 3, 4, "a", "b", "c"], 2))

    print(chunk_list([1, 2, 3, 4], 3))
