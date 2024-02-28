'''
735. Asteroid Collision
'''

from typing import List

def asteroidCollision0(asteroids: List[int]) -> List[int]:
    stack = []

    for i in range(len(asteroids)-1, -1, -1):
        if not asteroids:
            return []
        
        print("\nasteroids[i]:", asteroids[i], " asteroids[i-1]:", asteroids[i-1])
        print(asteroids)

        if asteroids[i] > 0 and asteroids[i-1] > 0:
            stack.append(asteroids[i])
            # stack.append(asteroids[i-1])
        else:
            if len(asteroids) >= 2:
                print("kaam kiya")
                # return
                if abs(asteroids[i]) > abs(asteroids[i-1]):
                    print("phele kaam kiya")
                    asteroids.pop(i-1)
                elif abs(asteroids[i]) < abs(asteroids[i-1]):
                    print("dosra kaam kiya")
                    asteroids.pop(i)
                else:
                    print("tesra kaam kiya")
                    asteroids.pop(i-1)
                    asteroids.pop(i)
            else:
                break

        print(asteroids)
    return asteroids




def asteroidCollision(asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            print("\nasteroid:", asteroid)
            while stack and stack[-1] > 0 and asteroid < 0:
                print(stack)
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    print("if chala")
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    print("elif chala")
                    stack.pop()
                break  # Break the loop to avoid unnecessary additions to the stack
            else:
                stack.append(asteroid)

        return stack


print(asteroidCollision([5,10,-5]))
# print(asteroidCollision([8,-8]))
# print(asteroidCollision([10,2,-5]))
# print(asteroidCollision([-2,-1,1,2]))




