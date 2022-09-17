import grpc 
import test_pb2
import test_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_pb2_grpc.SquareRootServiceStub(channel)
        response = stub.SquareRoot(test_pb2.Number(input=3))
        
        print(response.resulta)
    
if __name__ == '__main__':
    run()