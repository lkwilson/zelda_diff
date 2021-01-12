import struct
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

with open(f'zelda{start}.save', 'rb') as start_data_f:
  start_data = start_data_f.read()
  with open(f'zelda{end}.save', 'rb') as end_data_f:
    end_data = end_data_f.read()
    out_save = end_data
    type_id = 'h'
    type_size = 2
    for i in range(max(len(start_data), len(end_data))):
      try:
        val = struct.unpack(type_id, start_data[i:i+type_size])
        if val[0] != start:
          continue
      except:
        continue
      try:
        val = struct.unpack(type_id, end_data[i:i+type_size])
        if val[0] != end:
          continue
      except:
        continue
      print(i)
      out_save = out_save[:i] + struct.pack(type_id, 200) + out_save[i+type_size:]
    with open('hack.save', 'wb') as hack:
      hack.write(out_save)

