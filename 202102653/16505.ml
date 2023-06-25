let board = Array.make_matrix 1024 1024 ' '

let rec fillStar cnt row col =
	if cnt = 0 then board.(row).(col) <- '*'
  else
	let pow_cnt = int_of_float (2.0 ** float_of_int (cnt - 1)) in
    	fillStar (cnt - 1) row col;
    	fillStar (cnt - 1) (row + pow_cnt) col;
    	fillStar (cnt - 1) row (col + pow_cnt)

let print n =
  	let m = int_of_float (2.0 ** float_of_int n) in
  	for i = 0 to m - 1
    	do
		for j = 0 to m - i - 1 
		do
      			print_char board.(i).(j)
    		done;
    	print_newline ()
  	done

let () =
  	let n = read_int () in
  	fillStar n 0 0;
  	print n

