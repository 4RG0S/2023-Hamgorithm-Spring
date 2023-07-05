let _ = 
  let n = read_int () in 
  let max_five = n / 5 in
  let sol = ref (-1) in
  for i = 0 to max_five do
    let rem = n - i * 5 in
    let j = rem / 2 in
    let rem = rem - j * 2 in
    if rem = 0 then sol := i + j
    else ()
  done;
  Format.printf "%d" !sol
