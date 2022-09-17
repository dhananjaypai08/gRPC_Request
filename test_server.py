from concurrent import futures 
import test_pb2_grpc
import test_pb2
import grpc

class SquareRootServiceServicer(test_pb2_grpc.SquareRootServiceServicer):
    def SquareRoot(self, request, context):
        resulta = request.input * request.input
        return test_pb2.Result(resulta=resulta)
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_SquareRootServiceServicer_to_server(SquareRootServiceServicer(), server)
    print("Server Started...")
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()