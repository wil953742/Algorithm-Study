def solution(routes):
    routes.sort(key=lambda x:x[1])
    cam = [routes[0]]
    for i in range(1, len(routes)):
        drive_in = routes[i][0]
        last_cam = cam[len(cam)-1]
        last_cam_in, last_cam_out = last_cam[0], last_cam[1]

        if last_cam_out < drive_in:
            cam.append(routes[i])
        else:
            if drive_in < last_cam_in:
                pass
            else:
                cam[len(cam)-1] = [drive_in,last_cam_out]

    return len(cam)

sol = solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])
print(sol) #2