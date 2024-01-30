from random import randbytes


def unitByteConversion(bytes: int):
  """bytes -> KB | MB | GB | TB"""
  if not bytes:
    return '0 B'
  UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
  i = 0
  while (1):
    if bytes <= pow(1024, i + 1):
      break
    i += 1
  result = round(bytes / pow(1024, i), 2)
  return f'{result} {UNITS[i]}'


def uuid_v4():
  return ''.join(hex(byte)[2:].ljust(2, '0') for byte in randbytes(16))
