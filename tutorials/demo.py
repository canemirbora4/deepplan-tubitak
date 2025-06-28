from bulletarm import env_factory
import time
import pybullet as pb

def runDemo():
  env_config = {
        'render': True,
        'gui': True,
        'fast': False,
  }
  env = env_factory.createSingleProcessEnv('close_loop_drawer_opening', env_config)
  time.sleep(1)

  pb.setRealTimeSimulation(1)          # ← client id gerekmez

  pb.resetDebugVisualizerCamera(
        cameraDistance=1.5,
        cameraYaw=90,
        cameraPitch=-30,
        cameraTargetPosition=[0, 0, 0]
    )

  obs = env.reset()
  for _ in range(1000):
        try:
            action = env.getNextAction()
            obs, reward, done = env.step(action)
            time.sleep(0.2)
        except Exception as e:
            print(" EXIT", e)
            break

if __name__ == '__main__':
  runDemo()
