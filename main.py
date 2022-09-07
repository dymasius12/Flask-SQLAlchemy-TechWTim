

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Creating the model of our database
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"

# After you run once with the db.create_all please comment so you dont keep populating the database
# db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=str, help="Likes of the video", required=True)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# videos = {}

# def abort_if_video_id_doesnt_exist(video_id):
#     if video_id not in videos:
#         abort(404, message="Could not find the video..")

# def abort_if_video_exists(video_id):
#     if video_id in videos:
#         abort(404, message="Video already exist with that id..")

class Video(Resource):
    # Basically return the resource field as json
    @marshal_with(resource_fields) 
    def get(self, video_id):
        # abort_if_video_id_doesnt_exist(video_id)

        # Filter all the video by id and get the first entry that is filtered by.
        result = VideoModel.query.filter_by(id=video_id).first()
        # return videos[video_id]
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        # abort_if_video_exists(video_id)
        # args = video_put_args.parse_args()
        # videos[video_id] = args
        # return videos[video_id], 201
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="video id taken.. ")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, "/video/<int:video_id>")


# names = {"tim": {"age": 19, "gender": "male"},
#         "bill" : {"age": 70, "gender" : "male"}}

# class HelloWorld(Resource):
#     def get(self, name):
#         return names[name]

# We are registering the class HelloWorld from above and if user goes to /helloworld it will call the get request
# api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    # please comment below if run in production environment
    app.run(debug=True)

