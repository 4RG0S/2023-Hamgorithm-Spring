let rec findMaxProfit (tempDate : int) (numberOfRestDate : int) (consultingArr : (int * int) array) : int =
	(* Condition for exit findMaxProfit *)
	if tempDate >= numberOfRestDate then 0
	else
	
    		let t, p = consultingArr.(tempDate) in
		(* When take consulting in tempDate *)
    		let take = 
		if (tempDate + t <= numberOfRestDate) 
			then p + (findMaxProfit (tempDate + t) numberOfRestDate consultingArr) 
		else 0 in
    		
		(* When skip consulting in tempDate *)
		let skip = findMaxProfit (tempDate + 1) numberOfRestDate consultingArr in
    		max take skip

let main () =
  	(* Input *)
	let numberOfRestDate : int = read_int () in
  	
	(* Delcare Array *)
	let consultingArr : (int * int) array = Array.make numberOfRestDate (0, 0) in
  	
	(* Array Input & Setting *)
	for i = 0 to numberOfRestDate - 1 
	do
    		let t, p = Scanf.scanf "%d %d\n" (fun x y -> x, y) in
    		consultingArr.(i) <- (t, p)
  	done;
	
	(* Get result through function findMaxProfit *)
  	let result : int = findMaxProfit 0 numberOfRestDate consultingArr in
  	
	(* Output *)
	print_int result

let () = main ()
