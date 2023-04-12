#include <iostream>
#include <string>
#include <map>


int main()
{
  std::cin.tie(NULL);
  std::ios::sync_with_stdio(false);

  std::map<std::string, std::string> map;

  int N, M;
  std::cin >> N >> M;
  for (int i = 0; i < N; ++i)
  {
    std::string key, value;
    std::cin >> key >> value;
    map.insert({key, value});
  }
  for (int i = 0; i < M; ++i)
  {
    std::string key;
    std::cin >> key;
    std::cout << (*map.find(key)).second << "\n";
  }

  return 0;
}

// module MyMap = Map.Make(String);;

// let _ = 
//   let n, m = (Scanf.scanf "%d %d" (fun a b -> a, b)) in
//   let rec read_passwords (n : int) map = 
//     if n = 0 then map
//     else 
//       (
//         let line = input_line stdin in 
//         let sentences = String.split_on_char ' ' line in 
//         let key, value = (
//           match sentences with
//           | key :: value :: _ -> key, value
//           | _ -> failwith "input fail"
//         ) in 
//         read_passwords (n-1) (MyMap.add key value map)
//       )
//   in 
//   let map = read_passwords n MyMap.empty in 
//   let rec solve m map = 
//     if m = 0 then ()
//     else
//       let value = MyMap.find (read_line ()) map in 
//       let _ = Format.printf "%s\n" value in 
//       solve (m-1) map
//   in
//   solve m map