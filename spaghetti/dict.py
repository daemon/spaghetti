def flattened(obj):
  def merge(d1, d2):
    d = d1.copy()
    for k, v in d2.items():
      d[k].extend(v)
    return d
  table = defaultdict(list)
  if isinstance(obj, dict):
    for k, v in obj.items():
      if isinstance(v, dict) or isinstance(v, list) or isinstance(v, tuple):
        table = merge(table, flattened(v))
      else:
        table[k].append(v)
  elif isinstance(obj, list) or isinstance(obj, tuple):
    for x in obj:
      table = merge(table, flattened(x))
  return table