'''
@Date: 2020-03-21 10:59:11
@FilePath: /Wilson79/GitHub/Python_In_Action/faker/faker_1.py
@LastEditors: cs_shwei@163.com
@LastEditTime: 2020-04-19 17:59:53
'''
from faker import Faker
fake = Faker()  # 初始化

for i in range(30):
    print(fake.name())
    # print(fake.address())
    # print(fake.text())
    print("----------")

"""
Brett Scott
501 Juan Isle
Justinview, MT 17852
Herself everyone others. Arm argue indeed officer. Dog risk center past want generation these. Year give collection research.
----------
Timothy Rosario
8079 Alison Plains
Lake Kathyton, WY 92893
Sport white thought down send for approach. Eye since amount.
Leader your north move. Sea direction forward car.
Sing way information different first couple. Him anyone that life similar.
----------
Robert Vasquez
39684 Hale Knoll Apt. 067
South Gabrielland, MN 04757
Ten name hit involve yourself line. Since indeed hard range.
Perhaps just cut girl couple family. Best fall join occur statement pressure. Near according she figure director her.
----------
"""
