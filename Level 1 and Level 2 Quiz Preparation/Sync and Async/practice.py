#----------Sync Example----------

import time

# Step 1
print("Car is starting.......")
time.sleep(5)
print("Car is started.")

# Step 2
print("PC is turning on.......")
time.sleep(5)
print("PC is turned on.")

#----------Async Example----------

# import asyncio

# async def car_starting():
#     print("Car is starting.......")
#     await asyncio.sleep(5)
#     print("Car is started.")

# async def pc_turning_on():
#     print("PC is turning on.......")
#     await asyncio.sleep(5)
#     print("PC is turned on.")

# async def main():
#     await asyncio.gather(
#         car_starting(),
#         pc_turning_on()
#     )

# asyncio.run(main())