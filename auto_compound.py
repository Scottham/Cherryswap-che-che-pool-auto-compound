import time
import harvest_and_restake
import settings


gas_used = 0
order_number = 1
loop_status = 1
restake_value = 0

while loop_status == 1:
    print("Order: %i" % order_number)
    harvest = harvest_and_restake.harvest_and_restake(1,0)
    restake_value = harvest.harvest_amount
    gas_used = gas_used+harvest.gas_consume
    
    if harvest.transaction_status == 1:
        restake = harvest_and_restake.harvest_and_restake(0,harvest.harvest_amount)
        gas_used = gas_used+restake.gas_consume
        if restake.transaction_status == 0:
            loop_status = 0
    else:
        loop_status = 0
    
    print("Restaked amount (estimated): %f" % (restake_value/(1e+18)))
    print("Gas Used: %f" % (gas_used/(1e+18)))
    
    now = time.localtime()
    nowt = time.strftime("%Y-%m-%d-%H:%M:%S", now)
    print(nowt)
    
    print("Please wait for: %d minutes" % settings.harvest_interval)

    order_number = order_number + 1
    
    time.sleep(settings.harvest_interval*60)
    
