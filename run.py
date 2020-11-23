import struct
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

with open(f'zelda{start}.save', 'rb') as start_data_f:
  start_data = start_data_f.read()
  with open(f'zelda{end}.save', 'rb') as end_data_f:
    end_data = end_data_f.read()
    out_save = end_data
    for i in range(max(len(start_data), len(end_data))):
      try:
        val = struct.unpack('i', start_data[i:i+4])
        if val[0] != start:
          continue
      except:
        continue
      try:
        val = struct.unpack('i', end_data[i:i+4])
        if val[0] != end:
          continue
      except:
        continue
      print(i)
      out_save = out_save[:i] + struct.pack('i', 200) + out_save[i+4:]
    with open('hack.save', 'wb') as hack:
      hack.write(out_save)

