import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 1234
person.name = "Ben Dover"
person.email = "bendover@ben.com"
phone = person.phones.add()
phone.number = "555333222"
phone.type = addressbook_pb2.Person.HOME

print("Is initialized: ", person.IsInitialized())
print(person)

serializedData = person.SerializeToString()
print("Serialized Data: ", serializedData)

print("---------------------------------")

person2 = addressbook_pb2.Person()
person2.ParseFromString(serializedData)
print(person)