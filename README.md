# ipv6-目录爆破
ipv6目录爆破工具
市面上一直没有一个好的ipv6爆破工具就自己写了一个
使用方法 -i是ipv6的地址位置 -l是目录的地址位置 -o是输出的文件
python ipv6.py -i ipv6_addresses.txt -l directories.txt -o output.csv

	parser.add_argument("-i", "--ipv6", type=str, help="包含 IPv6 地址的文件路径")
	parser.add_argument("-l", "--directories", type=str, help="包含目录列表的文件路径")
	parser.add_argument("-o", "--output", type=str, help="输出结果的文件路径最后是csv路径")


不想安装库的话可以直接下exe版本的
ipv6.exe -i ipv6_addresses.txt -l directories.txt -o output.csv
使用截图
![image](https://github.com/user-attachments/assets/86777000-9a10-49f2-9f47-1ec2c70942e1)
