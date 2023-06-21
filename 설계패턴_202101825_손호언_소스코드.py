import time
from abc import ABC, abstractmethod


class Plant:
    def __init__(self, name):
        self.name = name
        self.growth = 0

    def grow(self):
        self.growth += 10
        print(f"{self.name} has grown 10%. Current growth: {self.growth}%")
        if self.growth >= 100:
            print(f"{self.name}의 성장이 완료되었습니다. 재배를 시작하세요!")

# Command 패턴


class Command(ABC):
    @abstractmethod
    def execute(self, plant):
        pass


class WateringCommand(Command):
    def execute(self, plant):
        print("물을 주는 중...")
        print()
        print("| | | | |")
        print(" | | | | |")
        print("| | | | |")
        print()
        time.sleep(self.wait_time)
        print("물 주기 작업 완료!")
        plant.grow()


class NutritionSupplyCommand(Command):
    def execute(self, plant):
        print("영양분을 공급하는 중...")
        print()
        print("* * * * *")
        print(" * * * * *")
        print("* * * * *")
        print()
        time.sleep(self.wait_time)
        print("영양분 공급 작업 완료!")
        plant.grow()


class PestControlCommand(Command):
    def execute(self, plant):
        print("해충을 관리하는 중...")
        print()
        print("- - 윙윙 - -")
        print("- - - - - - ")
        print("- - 깨꼬닥 - -")
        print()
        time.sleep(self.wait_time)
        print("해충 관리 작업 완료!")
        plant.grow()


class SunlightControlCommand(Command):
    def execute(self, plant):
        print("햇빛을 조절하는 중...")
        print()
        print("-o-")
        print()
        time.sleep(self.wait_time)
        print("햇빛 조절 작업 완료!")
        plant.grow()
# Strategy 패턴


# Strategy 패턴
class PlantCareStrategy(ABC):
    @abstractmethod
    def execute_command(self, command: Command, plant: Plant):
        pass


class CactusCareStrategy(PlantCareStrategy):
    def __init__(self):
        self.wait_times = {
            WateringCommand: 2,
            NutritionSupplyCommand: 2,
            PestControlCommand: 2,
            SunlightControlCommand: 2
        }

    def execute_command(self, command: Command, plant: Plant):
        command.wait_time = self.wait_times[type(command)]
        command.execute(plant)


class RoseCareStrategy(PlantCareStrategy):
    def __init__(self):
        self.wait_times = {
            WateringCommand: 3,
            NutritionSupplyCommand: 1,
            PestControlCommand: 5,
            SunlightControlCommand: 1
        }

    def execute_command(self, command: Command, plant: Plant):
        command.wait_time = self.wait_times[type(command)]
        command.execute(plant)


class TomatoCareStrategy(PlantCareStrategy):
    def __init__(self):
        self.wait_times = {
            WateringCommand: 4,
            NutritionSupplyCommand: 3,
            PestControlCommand: 5,
            SunlightControlCommand: 3
        }

    def execute_command(self, command: Command, plant: Plant):
        command.wait_time = self.wait_times[type(command)]
        command.execute(plant)

# Facade 패턴


class AutomatedPlantCareSystemFacade:
    def __init__(self):
        self.care_commands = {
            "물주기": WateringCommand(),
            "영양분공급": NutritionSupplyCommand(),
            "해충관리": PestControlCommand(),
            "햇빛조절": SunlightControlCommand()
        }
        self.plant_care_strategies = {
            "선인장": CactusCareStrategy(),
            "장미": RoseCareStrategy(),
            "방울토마토": TomatoCareStrategy()
        }

    def manage_plant(self):
        plant_type = input("어떤 식물을 관리하시겠습니까?(선인장/장미/방울토마토)")
        while plant_type not in self.plant_care_strategies:
            print("존재하지 않는 식물입니다")
            plant_type = input("어떤 식물을 관리하시겠습니까? ")

        plant = Plant(plant_type)
        strategy = self.plant_care_strategies[plant_type]
        more_to_care = True

        while more_to_care:
            care_command = input("어떤 관리를 실행하시겠습니까?(물주기/해충관리/영양분공급/햇빛조절) ")
            while care_command not in self.care_commands:
                print("수행할 수 없는 작업입니다")
                care_command = input("어떤 관리를 실행하시겠습니까? ")

            strategy.execute_command(self.care_commands[care_command], plant)

            more = input("다른 관리를 더 진행합니까? (Y/N) ")
            while more not in ['Y', 'N']:
                print("잘못된 입력입니다")
                more = input("다른 관리를 더 진행합니까? (Y/N) ")

            more_to_care = True if more == 'Y' else False
            if not more_to_care:
                print("식물 관리 시스템을 종료합니다.")


def main():
    system = AutomatedPlantCareSystemFacade()
    system.manage_plant()


if __name__ == "__main__":
    main()
