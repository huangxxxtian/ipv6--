# ipv6-
ipv6目录爆破工具
市面上一直没有一个好的ipv6爆破工具就自己写了一个
使用方法 -i是ipv6的地址位置 -l是目录的地址位置 -o是输出的文件
python ipv6.py -i ipv6_addresses.txt -l directories.txt -o output.csv

	parser.add_argument("-i", "--ipv6", type=str, help="包含 IPv6 地址的文件路径")
	parser.add_argument("-l", "--directories", type=str, help="包含目录列表的文件路径")
	parser.add_argument("-o", "--output", type=str, help="输出结果的文件路径最后是csv路径")
