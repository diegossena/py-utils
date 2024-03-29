from random import randbytes


def unitByteConversion(bytes: int) -> str:
  """unitByteConversion(100) -> \"100 B\""""
  UNITS = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
  i = 0
  while (bytes > pow(1024, i + 1)):
    i += 1
  result = round(bytes / pow(1024, i), 2)
  return f'{result} {UNITS[i]}'


def uuid() -> str:
  return ''.join(hex(byte)[2:].ljust(2, '0') for byte in randbytes(16))
