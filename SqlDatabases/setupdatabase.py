from basic import db,Puppy

#Creates all the Tables Model
db.create_all()

sam = Puppy('sammy',3)
frank = Puppy('Frankie',7)

print(sam.id)
print(frank.id)

db.session.add_all([sam,frank]) 

db.session.commit()


print(sam.id)
print(frank.id) 