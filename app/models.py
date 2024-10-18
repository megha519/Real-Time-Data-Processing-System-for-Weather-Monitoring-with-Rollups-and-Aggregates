from app import db

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    main = db.Column(db.String(50))
    temp = db.Column(db.Float)
    feels_like = db.Column(db.Float)
    date_time = db.Column(db.DateTime)

    def __repr__(self):
        return f"<WeatherData {self.city} at {self.date_time}>"

