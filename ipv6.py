import argparse
import requests
import csv


def read_list_from_file(filename):
	with open(filename, 'r', encoding='utf-8') as f:
		lines = [line.strip() for line in f if line.strip()]
	return lines


def check_ipv6_address(address):
	if not address.startswith("http://") and not address.startswith("https://"):
		address = "http://" + address
	return address


def access_ipv6_addresses(addresses, directories, output_filename):
	with open(output_filename, 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(["IPv6地址", "目录", "响应状态码", "返回包大小"])

		for address in addresses:
			for directory in directories:
				if not directory.startswith('/'):
					directory = '/' + directory
				url = address + directory
				try:
					response = requests.get(url)
					status_code = response.status_code
					if status_code < 500:
						content_size = len(response.content)
						row = [address, directory, status_code, content_size]
						writer.writerow(row)
						print(f"访问 {url} 的响应状态码: {status_code}，返回包大小: {content_size} bytes")
				except requests.exceptions.RequestException as e:
					error_message = str(e)
					print(f"访问 {url} 时出错: {error_message}")

	print(f"结果已保存到文件 {output_filename}")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="批量访问 IPv6 地址的目录")
	parser.add_argument("-i", "--ipv6", type=str, help="包含 IPv6 地址的文件路径")
	parser.add_argument("-l", "--directories", type=str, help="包含目录列表的文件路径")
	parser.add_argument("-o", "--output", type=str, help="输出结果的文件路径最后是csv路径")
	args = parser.parse_args()

	ipv6_filename = args.ipv6
	directories_filename = args.directories
	output_filename = args.output

	ipv6_addresses = read_list_from_file(ipv6_filename)
	directories = read_list_from_file(directories_filename)

	if ipv6_addresses and directories:
		ipv6_addresses = [check_ipv6_address(address) for address in ipv6_addresses]
		access_ipv6_addresses(ipv6_addresses, directories, output_filename)
	else:
		print(f"从文件 {ipv6_filename} 或 {directories_filename} 中没有读取到有效的 IPv6 地址或目录。")
