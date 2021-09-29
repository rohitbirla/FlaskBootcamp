# Create enties into the table

from models import db,Puppy,Owner,Toy

rufus = Puppy('Rufus')
fido = Puppy('Fido')

#Add
db.session.add_all([rufus,fido])
db.session.commit()


#check
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Create Owner Object

jose  = Owner('jose',rufus.id)
# Give some toys

toy1 = Toy('Chew Toy',rufus.id)
toy2 = Toy('Ball',rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()


print(rufus.report_toys())
#Grabe rufus 
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)