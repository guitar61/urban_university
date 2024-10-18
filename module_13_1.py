import asyncio


async def start_strongman(name, power):
    print(f'Strongman {name} started the competition.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)  # The stronger the power, the shorter the delay
        print(f'Strongman {name} lifted stone {i}')
    print(f'Strongman {name} finished the competition.')


async def start_tournament():
    # Create tasks for three strongmen with different names and power levels
    task1 = asyncio.create_task(start_strongman('Pash', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))

    # Wait for all tasks (strongmen) to finish
    await task1
    await task2
    await task3


# Run the tournament
asyncio.run(start_tournament())
