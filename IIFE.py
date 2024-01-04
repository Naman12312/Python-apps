import asyncio

import time
async def main(n):
    await asyncio.sleep(n)
    return True

async def main2(n):
    await asyncio.sleep(n)
    return True

t1 = time.perf_counter()
@lambda _:asyncio.run(_()) # IIFE: Immediately Invoked Function Expression
async def run():
    # results = asyncio.run(main(5))
    # results1 = asyncio.run(main2(5)) # 10 secs
    results = await asyncio.gather(main(5), main2(5)) # 5secs

    return results

t2 = time.perf_counter()
print(t2-t1)

