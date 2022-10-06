#!/usr/bin/python
# -*- coding: utf8 -*-
import sas as main_sas
import time
import binascii
import random
import string

sas=main_sas.sas('/dev/ttyS3')
sas.start()
#print sas.int_to_bcd(1234567890365421,8)
### EFT to machine
##for i in range(1,6):
##        a= sas.eft_load_cashable_credits( amount=10, count=i, status=0)
##        
##        print main_sas.aft_statement.get('eft_status')
##        print main_sas.aft_statement.get('eft_transfer_counter')
##        sas.eft_load_cashable_credits( amount=10, count=i+1, status=0)
##        
##        sas.eft_load_cashable_credits( amount=10, count=i+1, status=1)
##        sas.eft_avilable_transfers()
##        time.sleep(5)

#time.sleep(3)
##


#sas.startup()


########## AFT
###register
##sas.AFT_register_gaming_machine( reg_code=0x00,
##                                 asset_number=200,
##                                 reg_key=0x1234573657236575,
##                                 POS_ID=0xffffffff)
##
##sas.AFT_register_gaming_machine( reg_code=0x01,
##                                 asset_number=200,
##                                 reg_key=0x1234573657236575,
##                                 POS_ID=0xffffffff)
###lock
##sas.AFT_game_lock_and_status_request( lock_code=0x80,
##                                      transfer_condition=0b00000000,
##                                      lock_timeout=1)
##
###transfer
##sas.AFT_transfer_funds( transfer_code=0x00,
##                        transaction_index=0x00,
##                        transfer_type=0x00,
##                        cashable_amount=10000,
##                        restricted_amount=0,
##                        non_restricted_amount=0,
##                        transfer_flags=0b00000011,
##                        asset_number=b'\xea\x03\x00\x00' ,
##                        registration_key=0x1234573657236575,
##                        transaction_ID_lenght=0x01,
##                        transaction_ID='1',
##                        expiration=1,
##                        pool_ID=1,
##                        reciept_data=b'\x00'+'hey',
##                        lock_timeout=1)


##for keys, values in main_sas.aft_statement.items():
##        print(keys)
##        print(values)
##
##
while True:
        
        sas.send_meters_10_15()
        sas.current_credits()
        sas.eft_avilable_transfers()
        sas.AFT_game_lock_and_status_request( lock_code=0xff)
        state= binascii.hexlify(bytearray(sas.events_poll()))
        print(state)
        if (state=='51'): #cashout
                sas.eft_send_promo_to_machine( amount=25, status=a)



############cashout-cashin
        
        if (state=='57'): #cashout
                sas.pending_cashout_info()
                time.sleep(.5)
                sas.validation_number( validationID=1, valid_number=int(''.join([random.choice(string.digits) for n in range(16)])))
                
                sas.send_meters_10_15()
                print(main_sas.meters.get('total_in_meter'))
                print(main_sas.meters.get('total_out_meter'))
                sas.current_credits()
                print(main_sas.meters.get('current_credits'))
                
                #sas.cash_out_ticket_info()
                
        if (state=='67'): #cashin
                sas.ticket_validation_data()
                sas.redeem_ticket( transfer_code=0, transfer_amount=10000, parsing_code=0, validation_data=1234567891234567, rescticted_expiration=3, pool_ID=0)
                time.sleep(.3)
                sas.redeem_ticket( transfer_code=0xff, transfer_amount=10000, parsing_code=0, validation_data=1234567891234567, rescticted_expiration=3, pool_ID=0)

        #71
        
        time.sleep(1)

for keys, values in list(tito_statement.items()):
        print(keys)
        print(values)
