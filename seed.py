from app import create_app
from app.models import db, Hero, Power, HeroPower

app = create_app()

with app.app_context():
    print("🧨 Clearing old data...")
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    print("🦸 Adding heroes...")
    hero1 = Hero(name="Clark Kent", super_name="Superman")
    hero2 = Hero(name="Bruce Wayne", super_name="Batman")
    hero3 = Hero(name="Diana Prince", super_name="Wonder Woman")

    print("⚡ Adding powers...")
    power1 = Power(name="Flight", description="Gives the hero the ability to fly through the air at great speeds.")
    power2 = Power(name="Invisibility", description="Allows the hero to become invisible to the naked eye.")
    power3 = Power(name="Super Strength", description="Enhances the hero's strength far beyond human limits.")

    print("💥 Linking powers to heroes...")
    hp1 = HeroPower(strength="Strong", hero=hero1, power=power1)
    hp2 = HeroPower(strength="Average", hero=hero1, power=power3)
    hp3 = HeroPower(strength="Weak", hero=hero2, power=power2)
    hp4 = HeroPower(strength="Strong", hero=hero3, power=power3)

    db.session.add_all([hero1, hero2, hero3, power1, power2, power3, hp1, hp2, hp3, hp4])
    db.session.commit()

    print("✅ Database seeded successfully!")
