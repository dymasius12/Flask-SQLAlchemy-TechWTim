

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=str, help="Likes of the video", required=True)

videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find the video..")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(404, message="Video already exist with that id..")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

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

