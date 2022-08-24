import qrcode


def get_qrcode(url, name):
	qr = qrcode.make(data=url)
	qr.save(stream=f'{name}.png')

	return f'QR Code was created! Please open {name}.pnf file!'


def main():
	get_qrcode(
		url = input('Please Edit URL: '),
		name = input('Please Edit Name: ')
	)


if __name__ == '__main__':
	main()