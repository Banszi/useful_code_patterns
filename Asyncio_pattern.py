import asyncio


async def calculate_plus_one(number: int) -> int:
    return number + 1


async def main(example_data: list) -> list:
    '''
    add_to_first_elm = asyncio.create_task(calculate_plus_one(example_data[0]))
    add_to_second_elm = asyncio.create_task(calculate_plus_one(example_data[1]))
    add_to_third_elm = asyncio.create_task(calculate_plus_one(example_data[2]))

    asyncio_result = await asyncio.gather(add_to_first_elm, add_to_second_elm, add_to_third_elm)
    '''

    asyncio_tasks = [asyncio.create_task(calculate_plus_one(elm)) for elm in example_data]

    asyncio_result = await asyncio.gather(*asyncio_tasks)

    return asyncio_result


if __name__ == "__main__":

    example_data = [1,2,3]
    print(f'Data before: {example_data}')

    result = asyncio.run(main(example_data))

    print(f'Data after: {result}')