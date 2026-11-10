from api.controllers import Delivery
from django_mock_queries.query import MockSet, MockModel

def test_LotsOfItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  delivery_distance = 6
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 7.5

def test_MiddleOfTheRoadItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  delivery_distance = 4
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 5

def test_LittleItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=1))
  order.add(MockModel(quantity=1))
  order.add(MockModel(quantity=1))
  delivery_distance = 2
  #Act
  cost = Delivery.calculate(order, delivery_distance)
  #Assert
  assert cost == 2.5

def test_MoreThanTenItemsButDistanceIsNotMoreThanFive():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=11))
  delivery_distance = 5
  #Act
  cost = Delivery.calculate(order, delivery_distance)
  #Assert
  assert cost == 5

def test_MoreThanFiveItemsButDistanceIsNotMoreThanThree():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=6))
  delivery_distance = 3
  #Act
  cost = Delivery.calculate(order, delivery_distance)
  #Assert
  assert cost == 2.5

def test_FiveItemsDoNotQualifyForMiddleFee():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5))
  delivery_distance = 4
  #Act
  cost = Delivery.calculate(order, delivery_distance)
  #Assert
  assert cost == 2.5
