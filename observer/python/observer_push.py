"""
Implementation of Observer pattern, 'push' version.
'push' - meaning the Subject notifies the Observer every time the state is changed.

Test on the Westher data application.
For on of the Observers' implementations use 'numpy' 
"""

from numpy import mean

from abc import ABC, abstractmethod 

# -------------------------------------------------
# IMPLEMENTATION OF SUBJECT AND OBSERVER INTERFACES
# -------------------------------------------------

class Subject(ABC):
    @abstractmethod
    def register(*args):
        pass

    @abstractmethod
    def remove(*args):
        pass

    @abstractmethod
    def notify(*args):
        pass


class Observer(ABC):
    def __init__(self, subject):
        self.subscribe(subject)

    @abstractmethod
    def update(*args, **kwargs):
        pass

    # subscribe() and unsubscribe() for more comfortable user experience 
    def subscribe(self, subject):
        self.subject = subject
        self.subject.register(self)

    def unsubscribe(self):
        self.subject.remove(self)


# --------------------------------------------
# IMPLEMENTATION OF THE INTERFACES
# --------------------------------------------

# implement a Subject
class WeatherData(Subject):
    observers = []
    weather_conditions = {'temperature': None,
                          'pressure': None,
                          'humidity': None}
    
    @classmethod
    def update_condition(cls, condition_name: str, 
                              condition_value: object,
                              notifyObservers=True):
        cls.weather_conditions[condition_name] = condition_value
        if notifyObservers:
            cls.notify()
    
    def register(self, observer):
        if observer not in WeatherData.observers:
            WeatherData.observers.append(observer)
    
    def remove(self, observer):
        if observer in WeatherData.observers:
            observer_index = WeatherData.observers.index(observer)
            WeatherData.observers.pop(observer_index)
    
    @classmethod
    def notify(cls):
        [observer.update(cls.weather_conditions) for observer in cls.observers]



class Display():
    def display(self, *args):
        pass

# implement an one of the Observers 
class CurrentConditionsDisplay(Observer, Display):
    def __init__(self, subject):
        super().__init__(subject)

    def subscribe(self, subject):
        super().subscribe(subject)

    def unsubscribe(self):
        super().unsubscribe()
    
    def display(self, weather_conditions):
        content = "Current conditions:\n"
        content += "\n".join([f"{condition_name}: {condition_value}" for condition_name, 
                                                                         condition_value 
                                                                     in weather_conditions.items()]) \
                + "\n"
        print(content)
    
    def update(self, weather_conditions):
        self.display(weather_conditions)

# implement the other of the Observers 
class StatisticsDisplay(Observer, Display):
    def __init__(self, subject):
        super().__init__(subject)
        self.weather_conditions_statistics = {"temperature": [],
                                              "humidity": [],
                                              "pressure": []}


    def subscribe(self, subject):
        super().subscribe(subject)


    def unsubscribe(self):
        super().unsubscribe()


    def get_statistics(self, weather_conditions):
        """Calculates the mean value of each weather condition registered.
        returns a dictionary {condition_name: str: condition_value: float}
        """
        [self.weather_conditions_statistics[condition_name].append(condition_value) for condition_name, 
                                                                                        condition_value 
                                                                                    in weather_conditions.items()]
        weather_statistics = {condition_name: mean(condition_data) for condition_name, 
                                                                      condition_data 
                                                                  in self.weather_conditions_statistics.items()}
        return weather_statistics
    

    def display(self, weather_statistics):
        report_string = "\n".join([f"{condition}: {condition_statistics}" for condition, 
                                                                     condition_statistics 
                                                                 in weather_statistics.items()])
        content = "Weather statistics:\n" + report_string + "\n"
        print(content)


    def update(self, weather_conditions):
        weather_statistics = self.get_statistics(weather_conditions)
        self.display(weather_statistics)


# --------------------------------------------
# TESTING
# --------------------------------------------

if __name__ == "__main__":
    weather_station_data = WeatherData()

    current_condition_display = CurrentConditionsDisplay(weather_station_data)
    statistics_condition_display = StatisticsDisplay(weather_station_data)

    # START subject's state change
    weather_station_data.update_condition("temperature", 32, notifyObservers=False)
    weather_station_data.update_condition("humidity", 10.3, notifyObservers=False)
    weather_station_data.update_condition("pressure", 1013, notifyObservers=True)
    # END subject's state change

    # unsubscribe one of the observers
    statistics_condition_display.unsubscribe()
    # another way
    # weather_station_data.remove(statistics_condition_display)
    # one more different way
    # statistics_condition_display.subject.remove(statistics_condition_display) # under the hood is equivalent to the observer's unsubscribe() implementation

    # START subject's state change
    weather_station_data.update_condition("temperature", 33, notifyObservers=False)
    weather_station_data.update_condition("humidity", 13.3, notifyObservers=False)
    weather_station_data.update_condition("pressure", 999, notifyObservers=True)
    # END subject's state change

