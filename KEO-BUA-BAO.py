

import random
choices = ['kéo', 'búa', 'bao']

def get_machine_choice():
    return random.choice(choices)
player_choice = input("Nhập lựa chọn của bạn (kéo, búa, bao): ").strip().lower()

if player_choice != 'kéo' and player_choice != 'búa' and player_choice != 'bao':
    print("Lựa chọn không hợp lệ! Vui lòng chọn 'kéo', 'búa', hoặc 'bao'.")
else:
    
    machine_choice = get_machine_choice()
    print(f"Máy chọn: {machine_choice}")

    if player_choice == machine_choice:
        print("Hòa!")
    elif (player_choice == 'kéo' and machine_choice == 'búa') or \
         (player_choice == 'búa' and machine_choice == 'bao') or \
         (player_choice == 'bao' and machine_choice == 'kéo'):
        print("Bạn thắng!")
    else:
        print("Máy thắng!")