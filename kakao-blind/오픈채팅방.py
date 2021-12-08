def solution(record):
    answer = []
    nickname = {}
    
    for i in range(len(record)):
      record_list = record[i].split(' ')
      
      if len(record_list) > 2:
        command, id, name = record_list
      else:
        command, id = record_list
      
      msg = ""
      
      if command == "Enter":
        nickname[id] = name
        msg = "님이 들어왔습니다."
        
      elif command == "Change":
        nickname[id] = name
        
      else:
        msg = "님이 나갔습니다."
      
      if len(msg) > 0:
        answer.append([id, msg])
    
    
    return list(map(lambda x : nickname[x[0]] + x[1] , answer))
  
  
sol = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
print(sol)