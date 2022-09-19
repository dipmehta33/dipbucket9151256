import aws_cdk as core
import aws_cdk.assertions as assertions

from dipbucket9151256.dipbucket9151256_stack import Dipbucket9151256Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in dipbucket9151256/dipbucket9151256_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Dipbucket9151256Stack(app, "dipbucket9151256")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
